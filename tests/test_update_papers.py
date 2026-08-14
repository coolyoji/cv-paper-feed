import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import date, datetime
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "update_papers.py"
SPEC = importlib.util.spec_from_file_location("update_papers", MODULE_PATH)
update_papers = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = update_papers
SPEC.loader.exec_module(update_papers)


class FeedDateOverrideTests(unittest.TestCase):
    def test_feed_now_pins_retry_to_requested_date(self):
        with patch.object(update_papers, "FEED_DATE_OVERRIDE", "2026-07-25"):
            current = update_papers.feed_now()

        self.assertEqual(current.date(), date(2026, 7, 25))
        self.assertEqual(current.tzinfo, update_papers.UTC8)

    def test_feed_now_rejects_invalid_override(self):
        with (
            patch.object(update_papers, "FEED_DATE_OVERRIDE", "2026/07/25"),
            self.assertRaisesRegex(ValueError, "YYYY-MM-DD"),
        ):
            update_papers.feed_now()


class SourceFallbackTests(unittest.TestCase):
    def test_degraded_source_forces_cached_merge_above_count_threshold(self):
        with patch.object(update_papers, "SOURCE_DEGRADED", True):
            self.assertTrue(
                update_papers.should_merge_cached_candidates(
                    update_papers.MIN_FRESH_CANDIDATES + 1
                )
            )

    def test_complete_large_source_pool_does_not_force_cached_merge(self):
        with patch.object(update_papers, "SOURCE_DEGRADED", False):
            self.assertFalse(
                update_papers.should_merge_cached_candidates(
                    update_papers.MIN_FRESH_CANDIDATES
                )
            )


class CuratedNoteTests(unittest.TestCase):
    def test_experiment_takeaway_uses_verified_curated_evidence(self):
        paper = update_papers.Paper(
            title="Verified Paper",
            url="https://example.com/verified",
            summary="A generic summary.",
        )
        detail = (
            "研究问题：测试。方法与流程：测试。"
            "实验结论：AUROC为95.1，FPR95为19.9。"
            "迁移到COD时需要重新校准。"
        )
        with patch.object(
            update_papers,
            "load_abstract_details",
            return_value={paper.title: detail},
        ):
            takeaway = update_papers.experiment_takeaway(paper)

        self.assertEqual(takeaway, "AUROC为95.1，FPR95为19.9。")

    def test_experiment_takeaway_stops_before_analyst_boundary(self):
        paper = update_papers.Paper(
            title="Boundary-aware curated note",
            url="https://example.com/boundary",
            summary="A generic summary.",
        )
        detail = (
            "研究问题：测试。方法与流程：测试。"
            "实验结论：AUROC为95.1。"
            "分析边界：该分数不等于校准。"
        )
        with patch.object(
            update_papers,
            "load_abstract_details",
            return_value={paper.title: detail},
        ):
            takeaway = update_papers.experiment_takeaway(paper)

        self.assertEqual(takeaway, "AUROC为95.1。")

    def test_verified_curated_highlight_is_not_overwritten_by_cvf_abstract(self):
        paper = update_papers.Paper(
            title="Verified Short Summary",
            url="https://openaccess.thecvf.com/example.html",
            summary="人工核验的中文精炼摘要。",
            tags=["missing modality"],
            score=90,
        )
        sections = {"highlights": [paper]}

        with (
            patch.object(
                update_papers,
                "load_abstract_details",
                return_value={paper.title: "研究问题：已核验。方法与流程：已核验。"},
            ),
            patch.object(update_papers, "enrich_paper_abstracts") as enrich,
        ):
            update_papers.enrich_selected_sections(sections)

        enrich.assert_called_once_with([])
        self.assertEqual(paper.summary, "人工核验的中文精炼摘要。")
        self.assertEqual(paper.tags, ["missing modality"])

    def test_thermal_restoration_task_is_not_mislabeled_as_fire_detection(self):
        paper = update_papers.Paper(
            title="Calibration-Free Mobile Thermal Imaging",
            url="https://example.com/thermal-restoration",
            tags=["RGB-T", "thermal imaging", "image restoration"],
        )

        setting = update_papers.task_setting(paper)

        self.assertIn("热图超分", setting)
        self.assertIn("跨模态恢复", setting)
        self.assertNotIn("火焰/烟雾检测", setting)

    def test_apply_daily_curation_overrides_stale_cached_metadata(self):
        stale = update_papers.Paper(
            title="Curated Paper",
            url="https://example.com/stale",
            summary="Stale summary",
            tags=["stale"],
            score=99,
        )
        curated = update_papers.Paper(
            title="Curated Paper",
            url="https://example.com/verified",
            summary="Verified summary",
            tags=["verified"],
            score=1,
        )
        captured = {}

        def capture_history(papers, now, preserve_same_day_highlights=True):
            match = next(paper for paper in papers if paper.title == curated.title)
            captured["summary"] = match.summary
            captured["tags"] = match.tags
            return []

        with (
            patch.object(update_papers, "feed_now", return_value=datetime(2026, 8, 12, tzinfo=update_papers.UTC8)),
            patch.object(update_papers, "daily_curated_highlights", return_value=[curated]),
            patch.object(update_papers, "load_cached_candidate_pool", return_value=[stale]),
            patch.object(update_papers, "score_paper", return_value=50),
            patch.object(update_papers, "update_history", side_effect=capture_history),
            patch.object(update_papers, "render_existing_history"),
            patch.object(Path, "write_text"),
        ):
            update_papers.apply_daily_curation()

        self.assertEqual(captured["summary"], "Verified summary")
        self.assertEqual(captured["tags"], ["verified"])

    def test_specialized_transfer_papers_retain_their_actual_task_setting(self):
        cases = [
            (
                ["unknown label generation", "remote sensing"],
                "遥感开放世界目标检测与未知类命名",
            ),
            (["spatiotemporal segmentation"], "视频时空推理分割"),
            (
                ["spurious correlation", "multimodal prompt learning"],
                "跨模态 OOD 提示学习",
            ),
            (
                ["weakly supervised anomaly localization"],
                "图像级监督异常检测与定位",
            ),
            (["3D LiDAR anomaly segmentation"], "三维 LiDAR 开放集异常分割"),
            (["4D LiDAR generation"], "不确定性感知的 4D LiDAR 序列生成"),
            (
                ["open-world segmentation", "3D perception"],
                "开放世界可提示三维语义分割",
            ),
            (["open-world temporal grounding"], "开放世界视频时序定位"),
            (["video anomaly detection"], "视频异常检测与开放词汇异常识别"),
            (["degraded perception", "object detection"], "退化水下目标检测"),
            (
                ["selective prediction", "risk control"],
                "选择性预测与风险控制",
            ),
            (["trajectory prediction"], "多模态轨迹预测"),
            (["video understanding", "hazard perception"], "安全关键视频理解"),
        ]

        for tags, expected in cases:
            with self.subTest(tags=tags):
                paper = update_papers.Paper(
                    title="Transfer Paper",
                    url="https://example.com/transfer",
                    tags=tags,
                )
                self.assertIn(expected, update_papers.task_setting(paper))

    def test_daily_specialized_tags_produce_specific_transfer_notes(self):
        cases = [
            (["4D LiDAR generation"], "高不确定弱证据区域", "条件扩散补全"),
            (
                ["open-world segmentation", "3D perception"],
                "姿态与视角变化",
                "规范参考空间",
            ),
            (
                ["open-world temporal grounding"],
                "首次发现时间",
                "自纠边界",
            ),
            (["video anomaly detection"], "困难负文本", "区域文本对齐"),
            (
                ["degraded perception", "object detection"],
                "介质散射",
                "高频残差恢复",
            ),
        ]

        for tags, relation_phrase, borrow_phrase in cases:
            with self.subTest(tags=tags):
                paper = update_papers.Paper(
                    title="Specialized Paper",
                    url="https://example.com/specialized",
                    tags=tags,
                )
                self.assertIn(relation_phrase, update_papers.relation_to_topic(paper))
                self.assertIn(borrow_phrase, update_papers.borrow_points(paper))
                self.assertNotIn(
                    "可思考是否缺少",
                    update_papers.improvement_ideas(paper),
                )


class FireTopicTests(unittest.TestCase):
    def test_multispectral_fire_tag_requires_both_signals(self):
        tags = update_papers.derive_tags(
            "MSFireNet: Multispectral Wildfire Detection with RGB-T Fusion",
            "Visible and thermal infrared imagery are fused for early fire detection.",
            include_fire=True,
        )
        self.assertIn("multispectral fire", tags)

        satellite_tags = update_papers.derive_tags(
            "Active Fire Detection from VIIRS Observations",
            "A multi-band satellite method detects wildfire hotspots.",
            include_fire=True,
        )
        self.assertIn("multispectral fire", satellite_tags)

        unrelated_tags = update_papers.derive_tags(
            "Multispectral Pedestrian Detection",
            "The model fuses visible and infrared imagery for autonomous driving.",
            include_fire=True,
        )
        self.assertNotIn("multispectral fire", unrelated_tags)

    def test_fire_foundation_model_tag_requires_both_signals(self):
        tags = update_papers.derive_tags(
            "WildFireVLM: A Vision-Language Foundation Model for Wildfire Monitoring",
            "The model performs open-world smoke detection and fire localization.",
            include_fire=True,
        )
        self.assertIn("fire foundation model", tags)

        conventional_tags = update_papers.derive_tags(
            "Early Wildfire Detection with a Lightweight CNN",
            "A convolutional detector identifies smoke in camera images.",
            include_fire=True,
        )
        self.assertNotIn("fire foundation model", conventional_tags)

    def test_general_fire_perception_tag_covers_visible_smoke(self):
        tags = update_papers.derive_tags(
            "False Alarm Rectification for Early Smoke Segmentation",
            "Visible video separates early smoke from fog, cloud, and haze.",
            include_fire=True,
        )

        self.assertIn("fire perception", tags)
        self.assertNotIn("multispectral fire", tags)

    def test_fire_sections_prefer_formally_published_quality_sources(self):
        preprint = update_papers.Paper(
            title="Multispectral Wildfire Preprint",
            url="https://arxiv.org/abs/1",
            source="arXiv",
            published="2026-07-01",
            tags=["multispectral fire"],
            score=999,
        )
        conference = update_papers.Paper(
            title="Multispectral Wildfire Conference Paper",
            url="https://example.com/paper",
            source="CVPR 2025",
            published="2025",
            tags=["multispectral fire"],
            score=20,
        )

        sections = update_papers.select_feed_sections([preprint, conference])

        self.assertEqual(
            sections["fire_multispectral"][0].title,
            conference.title,
        )

    def test_new_sections_are_backward_compatible_and_rendered(self):
        legacy = update_papers.snapshot_sections({"sections": {"cod": []}})
        self.assertEqual(legacy["fire_multispectral"], [])
        self.assertEqual(legacy["fire_foundation"], [])

        paper = update_papers.Paper(
            title="WildFireVLM",
            url="https://example.com/wildfire-vlm",
            source="CVPR 2025",
            published="2025",
            summary="A vision-language foundation model monitors wildfire smoke.",
            tags=["fire foundation model"],
            score=80,
        )
        snapshot = update_papers.make_snapshot(
            [paper],
            datetime(2026, 7, 14, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )
        markdown = update_papers.render_snapshot_markdown(snapshot)

        self.assertIn("## 火灾/烟雾与多光谱感知", markdown)
        self.assertIn("## 火灾监测大模型", markdown)
        self.assertIn("WildFireVLM", markdown)
        self.assertIn("0 篇火灾/烟雾与多光谱感知", markdown)
        self.assertIn("1 篇火灾监测大模型", markdown)
        self.assertIn("本日未筛到可核验且达到质量阈值的候选", markdown)

    def test_fire_topics_start_on_july_14(self):
        self.assertFalse(update_papers.fire_topic_enabled(date(2026, 7, 13)))
        self.assertTrue(update_papers.fire_topic_enabled(date(2026, 7, 14)))

        paper = update_papers.Paper(
            title="WildFireVLM",
            url="https://example.com/wildfire-vlm",
            tags=["fire foundation model"],
            score=80,
        )
        july_13 = update_papers.make_snapshot(
            [paper],
            datetime(2026, 7, 13, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )
        markdown = update_papers.render_snapshot_markdown(july_13)
        self.assertNotIn("## 火灾/烟雾与多光谱感知", markdown)
        self.assertNotIn("## 火灾监测大模型", markdown)

    def test_daily_queries_cover_both_fire_directions(self):
        arxiv_queries = " ".join(update_papers.FIRE_ARXIV_QUERIES).lower()
        semantic_queries = " ".join(
            update_papers.FIRE_SEMANTIC_SCHOLAR_QUERIES
        ).lower()
        self.assertIn("multispectral fire detection", arxiv_queries)
        self.assertIn("fire monitoring", arxiv_queries)
        self.assertIn("multispectral", semantic_queries)
        self.assertIn("foundation model", semantic_queries)


class ExpandedResearchDirectionTests(unittest.TestCase):
    def test_every_requested_direction_has_search_coverage(self):
        query_corpus = " ".join(
            [
                *update_papers.RESEARCH_DIRECTION_ARXIV_QUERIES,
                *update_papers.RESEARCH_DIRECTION_SEMANTIC_SCHOLAR_QUERIES,
                *update_papers.FIRE_ARXIV_QUERIES,
                *update_papers.FIRE_SEMANTIC_SCHOLAR_QUERIES,
            ]
        ).lower()

        for direction in update_papers.EXPANDED_RESEARCH_DIRECTIONS:
            with self.subTest(direction=direction):
                self.assertIn(direction, query_corpus)
                self.assertIn(direction, update_papers.BROAD_KEYWORDS)

    def test_requested_direction_clusters_receive_specific_tags(self):
        tags = update_papers.derive_tags(
            "Risk-Controlling Prediction for Safety-Critical Video Hazard Anticipation",
            (
                "We study grounded visual reasoning and open-vocabulary visual grounding "
                "under missing modalities, degraded multimodal perception, and multimodal "
                "out-of-distribution shifts."
            ),
        )

        self.assertIn("safety-critical/hazard", tags)
        self.assertIn("grounded vision", tags)
        self.assertIn("multimodal robustness", tags)
        self.assertIn("selective/risk control", tags)
        self.assertIn("video anticipation", tags)

    def test_requested_directions_raise_transfer_priority(self):
        baseline = update_papers.Paper(
            title="A Generic Vision Method",
            url="https://example.com/generic",
            summary="A visual model is evaluated on a benchmark.",
            source="CVPR 2026",
        )
        targeted = update_papers.Paper(
            title="Selective Prediction for Open-World Multimodal Perception",
            url="https://example.com/targeted",
            summary=(
                "The method handles missing modality learning and multimodal "
                "out-of-distribution detection in safety-critical perception."
            ),
            source="CVPR 2026",
        )

        self.assertGreater(
            update_papers.score_paper(targeted),
            update_papers.score_paper(baseline),
        )


class HighlightHistoryTests(unittest.TestCase):
    def test_partial_source_pool_triggers_cached_candidate_merge(self):
        self.assertGreater(update_papers.MIN_FRESH_CANDIDATES, 775)

    @staticmethod
    def make_paper(title: str, score: int, url_suffix: str) -> object:
        return update_papers.Paper(
            title=title,
            url=f"https://example.com/{url_suffix}",
            source="CVPR 2026",
            published="2026",
            summary="An open-world uncertainty method for visual reasoning.",
            tags=["open-world", "uncertainty/calibration", "reasoning"],
            score=score,
        )

    def test_highlights_exclude_history_by_normalized_title(self):
        previous = self.make_paper("A Great Paper: Test!", 999, "previous")
        candidates = [
            self.make_paper("a great paper test", 999, "new-source"),
            *[
                self.make_paper(f"Fresh Paper {index}", 100 - index, f"fresh-{index}")
                for index in range(1, 6)
            ],
        ]

        selected = update_papers.select_highlights(
            candidates,
            update_papers.paper_identity_keys(previous),
        )

        self.assertEqual(len(selected), update_papers.HIGHLIGHT_LIMIT)
        self.assertNotIn("a great paper test", [paper.title for paper in selected])
        self.assertEqual(len({paper.title for paper in selected}), len(selected))

    def test_old_style_arxiv_ids_do_not_collide(self):
        first = update_papers.Paper(
            title="",
            url="https://arxiv.org/abs/cs/0601001",
        )
        second = update_papers.Paper(
            title="",
            url="https://arxiv.org/pdf/cs/0601002.pdf",
        )

        first_keys = update_papers.paper_identity_keys(first)
        second_keys = update_papers.paper_identity_keys(second)

        self.assertIn("arxiv:cs/0601001", first_keys)
        self.assertIn("arxiv:cs/0601002", second_keys)
        self.assertTrue(first_keys.isdisjoint(second_keys))

    def test_fallback_never_refills_with_historical_papers(self):
        previous = self.make_paper("Previously Read", 100, "previous")
        candidates = [
            previous,
            self.make_paper("Fresh One", 2, "fresh-one"),
            self.make_paper("Fresh Two", 1, "fresh-two"),
        ]
        for paper in candidates:
            paper.source = "Other"
            paper.published = ""
            paper.summary = ""
            paper.tags = []

        selected = update_papers.select_highlights(
            candidates,
            update_papers.paper_identity_keys(previous),
        )

        self.assertEqual([paper.title for paper in selected], ["Fresh One", "Fresh Two"])

    def test_same_day_fill_respects_pure_cod_limit(self):
        preserved = self.make_paper("Preserved COD", 100, "preserved-cod")
        preserved.tags = ["COD"]
        preserved.summary = ""
        second_cod = self.make_paper("Second COD", 99, "second-cod")
        second_cod.tags = ["COD"]
        second_cod.summary = ""
        fresh = self.make_paper("Fresh General Paper", 1, "fresh-general")
        fresh.source = "Other"
        fresh.published = ""
        fresh.tags = []
        fresh.summary = ""

        sections = update_papers.select_feed_sections(
            [second_cod, fresh],
            preserved_highlights=[preserved],
        )
        titles = [paper.title for paper in sections["highlights"]]

        self.assertIn(preserved.title, titles)
        self.assertNotIn(second_cod.title, titles)
        self.assertIn(fresh.title, titles)

    def test_update_history_excludes_prior_days(self):
        previous = self.make_paper("Previously Read", 999, "previous")
        candidates = [
            previous,
            *[
                self.make_paper(f"Fresh Paper {index}", 100 - index, f"fresh-{index}")
                for index in range(1, 6)
            ],
        ]
        old_snapshot = update_papers.make_snapshot(
            [previous],
            datetime(2026, 7, 12, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            history_file = Path(temp_dir) / "feed_history.json"
            history_file.write_text(
                json.dumps([old_snapshot], ensure_ascii=False),
                encoding="utf-8",
            )
            with (
                patch.object(update_papers, "HISTORY_FILE", history_file),
                patch.object(update_papers, "enrich_selected_sections"),
            ):
                history = update_papers.update_history(
                    candidates,
                    datetime(2026, 7, 13, 9, 10, tzinfo=update_papers.UTC8),
                )

        selected_titles = [
            item["title"] for item in history[0]["sections"]["highlights"]
        ]
        self.assertNotIn(previous.title, selected_titles)
        self.assertEqual(len(selected_titles), update_papers.HIGHLIGHT_LIMIT)
        self.assertEqual(history[1]["date"], "2026-07-12")

    def test_update_history_rejects_historical_daily_curation(self):
        previous = self.make_paper("Previously Curated", 999, "previous-curated")
        old_snapshot = update_papers.make_snapshot(
            [previous],
            datetime(2026, 7, 12, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir)
            history_file = data_dir / "feed_history.json"
            highlights_file = data_dir / "daily_highlights.json"
            history_file.write_text(
                json.dumps([old_snapshot], ensure_ascii=False),
                encoding="utf-8",
            )
            highlights_file.write_text(
                json.dumps(
                    {"2026-07-13": [update_papers.paper_to_dict(previous)]},
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            with (
                patch.object(update_papers, "HISTORY_FILE", history_file),
                patch.object(update_papers, "DAILY_HIGHLIGHTS_FILE", highlights_file),
                patch.object(update_papers, "enrich_selected_sections"),
            ):
                with self.assertRaisesRegex(
                    ValueError,
                    "Previously Curated",
                ):
                    update_papers.update_history(
                        [previous],
                        datetime(2026, 7, 13, 9, 10, tzinfo=update_papers.UTC8),
                    )

    def test_same_day_refresh_keeps_current_day_eligible(self):
        morning_candidates = [
            self.make_paper("Current Day Top Paper", 999, "top"),
            *[
                self.make_paper(f"Morning Paper {index}", 100 - index, f"morning-{index}")
                for index in range(1, 5)
            ],
        ]
        current_snapshot = update_papers.make_snapshot(
            morning_candidates,
            datetime(2026, 7, 13, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )
        rerun_candidates = [
            self.make_paper(f"Afternoon Paper {index}", 200 - index, f"afternoon-{index}")
            for index in range(1, 7)
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            history_file = Path(temp_dir) / "feed_history.json"
            history_file.write_text(
                json.dumps([current_snapshot], ensure_ascii=False),
                encoding="utf-8",
            )
            with (
                patch.object(update_papers, "HISTORY_FILE", history_file),
                patch.object(update_papers, "enrich_selected_sections"),
            ):
                history = update_papers.update_history(
                    rerun_candidates,
                    datetime(2026, 7, 13, 12, 30, tzinfo=update_papers.UTC8),
                )

        selected_titles = [
            item["title"] for item in history[0]["sections"]["highlights"]
        ]
        morning_titles = [
            item["title"]
            for item in current_snapshot["sections"]["highlights"]
        ]
        self.assertEqual(selected_titles, morning_titles)
        self.assertEqual(len(history), 1)

    def test_same_day_highlights_can_be_explicitly_reselected(self):
        morning_candidates = [
            self.make_paper(f"Morning Paper {index}", 100 - index, f"morning-{index}")
            for index in range(1, 6)
        ]
        current_snapshot = update_papers.make_snapshot(
            morning_candidates,
            datetime(2026, 7, 13, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )
        afternoon_candidates = [
            self.make_paper(
                f"Afternoon Paper {index}",
                200 - index,
                f"afternoon-{index}",
            )
            for index in range(1, 6)
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            history_file = Path(temp_dir) / "feed_history.json"
            history_file.write_text(
                json.dumps([current_snapshot], ensure_ascii=False),
                encoding="utf-8",
            )
            with (
                patch.object(update_papers, "HISTORY_FILE", history_file),
                patch.object(update_papers, "enrich_selected_sections"),
            ):
                history = update_papers.update_history(
                    afternoon_candidates,
                    datetime(2026, 7, 13, 12, 30, tzinfo=update_papers.UTC8),
                    preserve_same_day_highlights=False,
                )

        selected_titles = [
            item["title"] for item in history[0]["sections"]["highlights"]
        ]
        self.assertEqual(
            selected_titles,
            [paper.title for paper in afternoon_candidates],
        )

    def test_cached_candidate_pool_combines_latest_and_history_sections(self):
        latest_paper = self.make_paper("Latest Candidate", 80, "latest")
        history_paper = self.make_paper("History Candidate", 70, "history")
        snapshot = update_papers.make_snapshot(
            [history_paper],
            datetime(2026, 7, 12, 9, 10, tzinfo=update_papers.UTC8),
            enrich_abstracts=False,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir)
            (data_dir / "latest_papers.json").write_text(
                json.dumps([update_papers.paper_to_dict(latest_paper)]),
                encoding="utf-8",
            )
            history_file = data_dir / "feed_history.json"
            history_file.write_text(
                json.dumps([snapshot]),
                encoding="utf-8",
            )
            with (
                patch.object(update_papers, "DATA", data_dir),
                patch.object(update_papers, "HISTORY_FILE", history_file),
            ):
                cached = update_papers.load_cached_candidate_pool()

        self.assertEqual(
            {paper.title for paper in cached},
            {latest_paper.title, history_paper.title},
        )

    def test_history_key_reader_accepts_missing_sections(self):
        self.assertEqual(update_papers.history_highlight_keys([{"date": "2026-07-01"}]), set())


if __name__ == "__main__":
    unittest.main()
