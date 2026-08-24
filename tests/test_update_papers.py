import importlib.util
import json
import socket
import sys
import tempfile
import threading
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
    def test_crossref_stops_after_consecutive_source_failures(self):
        journal = {"issn": "0000-0000", "short": "TEST"}
        with (
            patch.object(update_papers, "TOP_JOURNALS", [journal]),
            patch.object(update_papers, "DEEP_SOURCE_SCAN", True),
            patch.object(update_papers, "SOURCE_FAILURE_LIMIT", 2),
            patch.object(update_papers, "fire_topic_enabled", return_value=False),
            patch.object(update_papers, "fetch_url", side_effect=TimeoutError("offline")) as fetch,
            patch.object(update_papers.time, "sleep"),
        ):
            self.assertEqual(update_papers.fetch_crossref_journals(), [])
        self.assertEqual(fetch.call_count, 2)

    def test_network_call_deadline_bounds_blocking_connector(self):
        blocker = threading.Event()
        closed = threading.Event()

        class LateResponse:
            def close(self):
                closed.set()

        def connect():
            blocker.wait(30)
            return LateResponse()

        with self.assertRaisesRegex(TimeoutError, "network operation exceeded 1s"):
            update_papers._call_with_deadline(connect, 1)
        blocker.set()
        self.assertTrue(closed.wait(1), "late response should be closed after timeout")

    def test_response_reader_converts_socket_timeout_to_deadline_error(self):
        class SlowResponse:
            def read(self, _size):
                raise socket.timeout("stalled")

        with self.assertRaisesRegex(TimeoutError, "response read exceeded 7s"):
            update_papers._read_response_with_deadline(SlowResponse(), 7)

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
            patch.object(update_papers, "require_verified_daily_notes"),
            patch.object(update_papers, "score_paper", return_value=50),
            patch.object(update_papers, "update_history", side_effect=capture_history),
            patch.object(update_papers, "render_existing_history"),
            patch.object(Path, "write_text"),
        ):
            update_papers.apply_daily_curation()

        self.assertEqual(captured["summary"], "Verified summary")
        self.assertEqual(captured["tags"], ["verified"])

    def test_existing_day_curation_preserves_non_highlight_sections(self):
        old_highlight = update_papers.Paper(
            title="Old Highlight",
            url="https://example.com/old",
        )
        curated = [
            update_papers.Paper(
                title=f"Curated {index}",
                url=f"https://example.com/curated-{index}",
            )
            for index in range(5)
        ]
        quality = {
            "title": "Quality Anchor",
            "url": "https://example.com/quality",
            "pdf": "",
            "authors": [],
            "source": "Test",
            "published": "2026",
            "summary": "Keep me byte-for-byte at the object level.",
            "tags": ["test"],
            "score": 42,
        }
        history = [
            {
                "date": "2026-08-20",
                "generated_at": "2026-08-20 10:28",
                "total_selected": 100,
                "sections": {
                    "highlights": [update_papers.paper_to_dict(old_highlight)],
                    "quality": [quality],
                },
            },
            {
                "date": "2026-08-19",
                "generated_at": "2026-08-19 10:28",
                "total_selected": 90,
                "sections": {"highlights": []},
            },
        ]

        result = update_papers.replace_existing_snapshot_curation(
            history, "2026-08-20", curated
        )

        self.assertEqual(result[0]["total_selected"], 100)
        self.assertEqual(result[0]["sections"]["quality"], [quality])
        self.assertEqual(
            [item["title"] for item in result[0]["sections"]["highlights"]],
            [paper.title for paper in curated],
        )

    def test_existing_day_curation_rejects_prior_section_duplicate(self):
        curated = [
            update_papers.Paper(
                title=f"Curated {index}",
                url=f"https://example.com/curated-{index}",
            )
            for index in range(5)
        ]
        history = [
            {
                "date": "2026-08-20",
                "sections": {"highlights": []},
            },
            {
                "date": "2026-08-19",
                "sections": {
                    "quality": [update_papers.paper_to_dict(curated[3])]
                },
            },
        ]

        with self.assertRaisesRegex(ValueError, "historical paper"):
            update_papers.replace_existing_snapshot_curation(
                history, "2026-08-20", curated
            )

    def test_existing_day_curation_rejects_later_highlight_duplicate(self):
        curated = [
            update_papers.Paper(
                title=f"Curated {index}",
                url=f"https://example.com/curated-{index}",
            )
            for index in range(5)
        ]
        history = [
            {"date": "2026-08-20", "sections": {"highlights": []}},
            {
                "date": "2026-08-21",
                "sections": {
                    "highlights": [update_papers.paper_to_dict(curated[2])]
                },
            },
        ]

        with self.assertRaisesRegex(ValueError, "historical paper"):
            update_papers.replace_existing_snapshot_curation(
                history, "2026-08-20", curated
            )

    def test_existing_day_curation_checks_new_prior_section_names(self):
        curated = [
            update_papers.Paper(
                title=f"Curated {index}",
                url=f"https://example.com/curated-{index}",
            )
            for index in range(5)
        ]
        history = [
            {"date": "2026-08-20", "sections": {"highlights": []}},
            {
                "date": "2026-08-19",
                "sections": {
                    "future_cluster": [update_papers.paper_to_dict(curated[4])]
                },
            },
        ]

        with self.assertRaisesRegex(ValueError, "historical paper"):
            update_papers.replace_existing_snapshot_curation(
                history, "2026-08-20", curated
            )

    def test_existing_day_curation_appends_paper_missing_from_latest(self):
        existing = update_papers.Paper(
            title="Existing",
            url="https://example.com/existing",
            summary="Old metadata",
        )
        replacement = update_papers.Paper(
            title="Existing",
            url="https://example.com/existing",
            summary="Verified metadata",
        )
        absent = update_papers.Paper(
            title="Absent curated paper",
            url="https://example.com/absent",
            score=2,
        )

        merged = update_papers.merge_curated_into_latest(
            [update_papers.paper_to_dict(existing)],
            [replacement, absent],
        )

        self.assertEqual(len(merged), 2)
        self.assertEqual(merged[0]["title"], "Absent curated paper")
        self.assertEqual(merged[1]["summary"], "Verified metadata")

    def test_latest_merge_preserves_different_title_arxiv_aliases(self):
        aliases = [
            update_papers.Paper(
                title="Original arXiv title",
                url="https://arxiv.org/abs/2608.12345v1",
                score=10,
            ),
            update_papers.Paper(
                title="Revised arXiv title",
                url="https://arxiv.org/abs/2608.12345v2",
                score=9,
            ),
        ]
        curated = update_papers.Paper(
            title="Official proceedings title",
            url="https://arxiv.org/abs/2608.12345v3",
            score=11,
        )

        merged = update_papers.merge_curated_into_latest(
            [update_papers.paper_to_dict(paper) for paper in aliases], [curated]
        )

        self.assertEqual(
            {item["title"] for item in merged},
            {
                "Original arXiv title",
                "Revised arXiv title",
                "Official proceedings title",
            },
        )

    def test_verified_highlight_metadata_prevents_placeholder_downgrade(self):
        title = (
            "RoFLIP: Robust and Fine-Grained Alignment for "
            "Vision-Language Compositional Reasoning"
        )
        placeholder = update_papers.Paper(
            title=title.upper(),
            url="https://doi.org/10.1007/s11263-026-02944-7",
            pdf="",
            source="Crossref / IJCV",
            summary="IJCV article matched by title; abstract unavailable.",
            score=98,
        )
        alias = update_papers.Paper(
            title="An Earlier Title for the Same RoFLIP Work",
            url="https://doi.org/10.1007/s11263-026-02944-7",
            summary="Keep this different-title alias.",
            score=90,
        )
        verified = update_papers.Paper(
            title=title,
            url="https://doi.org/10.1007/s11263-026-02944-7",
            pdf=(
                "https://link.springer.com/content/pdf/"
                "10.1007/s11263-026-02944-7.pdf"
            ),
            source=(
                "International Journal of Computer Vision (IJCV) 2026 / "
                "DOI:10.1007/s11263-026-02944-7"
            ),
            summary="人工核验的中文精读摘要。",
            score=86,
        )
        notes = {
            update_papers.normalized_note_title_key(title): {
                field: f"核验内容 / {field}"
                for field in update_papers.DAILY_NOTE_FIELDS
            }
        }

        with tempfile.TemporaryDirectory() as tmp:
            highlights_path = Path(tmp) / "daily_highlights.json"
            highlights_path.write_text(
                json.dumps(
                    {"2026-08-20": [update_papers.paper_to_dict(verified)]},
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            with patch.object(
                update_papers, "DAILY_HIGHLIGHTS_FILE", highlights_path
            ):
                restored = update_papers.overlay_verified_highlight_metadata(
                    [placeholder, alias], notes
                )

        self.assertEqual(restored[0], verified)
        self.assertEqual(restored[1], alias)
        self.assertEqual(
            len(
                {
                    update_papers.normalized_title_key(paper.title)
                    for paper in restored
                }
            ),
            2,
        )

    def test_verified_daily_note_overrides_generated_fields(self):
        paper = update_papers.Paper(
            title="Verified Paper",
            url="https://example.com/verified",
            summary="Fallback summary.",
        )
        note = {
            "一句话总结": "核验总结",
            "任务设定": "核验任务",
            "摘要详解": "核验摘要",
            "实验结论": "核验实验",
            "和我课题的关系": "核验关系",
            "可借鉴点": "核验借鉴",
            "可改进点": "核验改进",
            "是否值得精读": "核验结论",
        }

        with patch.object(
            update_papers,
            "load_daily_paper_notes",
            return_value={update_papers.normalized_note_title_key(paper.title): note},
        ):
            rendered = update_papers.md_paper_item(1, paper)

        for field_name, value in note.items():
            self.assertIn(f"- {field_name}：{value}", rendered)
        self.assertNotIn("Fallback summary", rendered)

    def test_verified_note_matches_normalized_title(self):
        paper = update_papers.Paper(
            title="Evidence & Reasoning: A Test",
            url="https://example.com/verified",
        )
        note = {field: f"核验{index}" for index, field in enumerate(update_papers.DAILY_NOTE_FIELDS)}
        with patch.object(
            update_papers,
            "load_daily_paper_notes",
            return_value={
                update_papers.normalized_note_title_key(
                    "Evidence &amp; Reasoning — A Test"
                ): note
            },
        ):
            rendered = update_papers.md_paper_item(1, paper)

        self.assertIn(f"- 摘要详解：{note['摘要详解']}", rendered)

    def test_compact_item_keeps_tracking_signal_without_full_note_schema(self):
        paper = update_papers.Paper(
            title="Compact Candidate",
            url="https://example.com/compact",
            pdf="https://example.com/compact.pdf",
            source="CVPR 2026",
            published="2026",
            tags=["uncertainty/calibration"],
        )

        rendered = update_papers.md_compact_paper_item(1, paper)

        self.assertIn("- 核心机制：", rendered)
        self.assertIn("- 跟踪理由：", rendered)
        self.assertIn("[pdf]", rendered)
        self.assertNotIn("- 摘要详解：", rendered)
        self.assertNotIn("- 可改进点：", rendered)

    def test_generated_abstract_explanation_obeys_compact_budget(self):
        sentence = "We propose " + "a" * 900 + "."
        paper = update_papers.Paper(
            title="Long Abstract",
            url="https://example.com/long",
            summary="Problem statement. " + sentence + " Results outperform baselines.",
        )

        explanation = update_papers.generated_abstract_explanation(paper)

        self.assertLessEqual(len(explanation), 900)
        self.assertIn("研究问题：", explanation)
        self.assertIn("方法主线：", explanation)
        self.assertIn("实验证据：", explanation)

    def test_verified_note_file_fails_closed_on_missing_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            notes_path = Path(tmp) / "notes.json"
            incomplete = {
                "Verified Paper": {
                    field: "核验内容"
                    for field in update_papers.DAILY_NOTE_FIELDS[:-1]
                }
            }
            notes_path.write_text(
                json.dumps(incomplete, ensure_ascii=False), encoding="utf-8"
            )
            update_papers.load_daily_paper_notes.cache_clear()
            try:
                with (
                    patch.object(update_papers, "DAILY_PAPER_NOTES_FILE", notes_path),
                    self.assertRaisesRegex(ValueError, "fields do not match"),
                ):
                    update_papers.load_daily_paper_notes()
            finally:
                update_papers.load_daily_paper_notes.cache_clear()

    def test_existing_day_apply_does_not_write_when_latest_is_invalid(self):
        curated = [
            update_papers.Paper(
                title=f"Curated {index}",
                url=f"https://example.com/curated-{index}",
            )
            for index in range(5)
        ]
        with tempfile.TemporaryDirectory() as tmp:
            data_dir = Path(tmp)
            history_path = data_dir / "feed_history.json"
            latest_path = data_dir / "latest_papers.json"
            history_path.write_text(
                json.dumps(
                    [
                        {
                            "date": "2026-08-20",
                            "sections": {"highlights": []},
                        }
                    ]
                ),
                encoding="utf-8",
            )
            original_history = history_path.read_bytes()
            latest_path.write_text("{broken", encoding="utf-8")

            with (
                patch.object(update_papers, "DATA", data_dir),
                patch.object(update_papers, "HISTORY_FILE", history_path),
                patch.object(
                    update_papers,
                    "feed_now",
                    return_value=datetime(2026, 8, 20, tzinfo=update_papers.UTC8),
                ),
                patch.object(
                    update_papers, "daily_curated_highlights", return_value=curated
                ),
                self.assertRaisesRegex(ValueError, "latest paper pool"),
            ):
                update_papers.apply_existing_daily_curation()

            self.assertEqual(history_path.read_bytes(), original_history)

    def test_render_existing_history_only_writes_requested_daily_snapshot(self):
        history = [
            {
                "date": "2026-08-20",
                "generated_at": "2026-08-20 10:00",
                "sections": {},
            },
            {
                "date": "2026-08-19",
                "generated_at": "2026-08-19 10:00",
                "sections": {},
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            daily_md = docs / "md"
            daily_html = docs / "html"
            with (
                patch.object(update_papers, "DOCS", docs),
                patch.object(update_papers, "DAILY_MD", daily_md),
                patch.object(update_papers, "DAILY_HTML", daily_html),
            ):
                update_papers.render_existing_history(
                    history, only_dates={"2026-08-19"}
                )

            self.assertTrue((docs / "literature.md").exists())
            self.assertTrue((docs / "index.html").exists())
            self.assertTrue((daily_md / "2026-08-19.md").exists())
            self.assertTrue((daily_html / "2026-08-19.html").exists())
            self.assertFalse((daily_md / "2026-08-20.md").exists())
            self.assertFalse((daily_html / "2026-08-20.html").exists())

    def test_atomic_batch_restores_replaced_files_when_commit_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.json"
            second = Path(tmp) / "second.json"
            first.write_text("first-before", encoding="utf-8")
            second.write_text("second-before", encoding="utf-8")
            real_replace = update_papers.os.replace
            calls = 0

            def fail_second_replace(source, destination):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("simulated commit failure")
                return real_replace(source, destination)

            with (
                patch.object(
                    update_papers.os, "replace", side_effect=fail_second_replace
                ),
                self.assertRaisesRegex(OSError, "simulated commit failure"),
            ):
                update_papers.write_text_batch_atomic(
                    {first: "first-after", second: "second-after"}
                )

            self.assertEqual(first.read_text(encoding="utf-8"), "first-before")
            self.assertEqual(second.read_text(encoding="utf-8"), "second-before")

    def test_atomic_batch_restores_replaced_files_on_keyboard_interrupt(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.json"
            second = Path(tmp) / "second.json"
            first.write_text("first-before", encoding="utf-8")
            second.write_text("second-before", encoding="utf-8")
            real_replace = update_papers.os.replace
            calls = 0

            def interrupt_second_replace(source, destination):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise KeyboardInterrupt()
                return real_replace(source, destination)

            with (
                patch.object(
                    update_papers.os, "replace", side_effect=interrupt_second_replace
                ),
                self.assertRaises(KeyboardInterrupt),
            ):
                update_papers.write_text_batch_atomic(
                    {first: "first-after", second: "second-after"}
                )

            self.assertEqual(first.read_text(encoding="utf-8"), "first-before")
            self.assertEqual(second.read_text(encoding="utf-8"), "second-before")

    def test_apply_daily_curation_validates_notes_before_history_update(self):
        with (
            patch.object(
                update_papers,
                "load_daily_paper_notes",
                side_effect=ValueError("invalid verified notes"),
            ),
            patch.object(update_papers, "update_history") as update_history,
            self.assertRaisesRegex(ValueError, "invalid verified notes"),
        ):
            update_papers.apply_daily_curation()

        update_history.assert_not_called()

    def test_existing_day_apply_preserves_non_target_daily_archives(self):
        curated = [
            update_papers.Paper(
                title=f"Curated {index}",
                url=f"https://example.com/curated-{index}",
                score=10 - index,
            )
            for index in range(5)
        ]
        verified_notes = {
            update_papers.normalized_note_title_key(paper.title): {
                field: f"{paper.title} / {field}"
                for field in update_papers.DAILY_NOTE_FIELDS
            }
            for paper in curated
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "data"
            docs = root / "docs"
            daily_md = docs / "md"
            daily_html = docs / "html"
            data.mkdir()
            daily_md.mkdir(parents=True)
            daily_html.mkdir(parents=True)
            history_path = data / "feed_history.json"
            latest_path = data / "latest_papers.json"
            history_path.write_text(
                json.dumps(
                    [
                        {
                            "date": "2026-08-20",
                            "generated_at": "2026-08-20 10:00",
                            "sections": {"highlights": []},
                        },
                        {
                            "date": "2026-08-19",
                            "generated_at": "2026-08-19 10:00",
                            "sections": {"highlights": []},
                        },
                    ]
                ),
                encoding="utf-8",
            )
            latest_path.write_text("[]", encoding="utf-8")
            older_md = daily_md / "2026-08-19.md"
            older_html = daily_html / "2026-08-19.html"
            older_md.write_bytes(b"older-md")
            older_html.write_bytes(b"older-html")

            with (
                patch.object(update_papers, "DATA", data),
                patch.object(update_papers, "DOCS", docs),
                patch.object(update_papers, "DAILY_MD", daily_md),
                patch.object(update_papers, "DAILY_HTML", daily_html),
                patch.object(update_papers, "HISTORY_FILE", history_path),
                patch.object(
                    update_papers,
                    "feed_now",
                    return_value=datetime(2026, 8, 20, tzinfo=update_papers.UTC8),
                ),
                patch.object(
                    update_papers, "daily_curated_highlights", return_value=curated
                ),
                patch.object(
                    update_papers,
                    "load_daily_paper_notes",
                    return_value=verified_notes,
                ),
            ):
                update_papers.apply_existing_daily_curation()

            self.assertEqual(older_md.read_bytes(), b"older-md")
            self.assertEqual(older_html.read_bytes(), b"older-html")
            self.assertTrue((daily_md / "2026-08-20.md").exists())
            self.assertTrue((daily_html / "2026-08-20.html").exists())
            written_history = json.loads(history_path.read_text(encoding="utf-8"))
            self.assertEqual(written_history[0]["total_selected"], 5)

    def test_specialized_transfer_papers_retain_their_actual_task_setting(self):
        cases = [
            (["wildfire UAV scale detection"], "UAV 图像火焰与烟雾目标检测"),
            (["latent entropy decoding"], "多模态大推理模型的解码期幻觉抑制"),
            (["saliency alignment reward"], "视觉语言推理的证据对齐训练"),
            (["prototype-guided 3D OOD"], "自动驾驶三维语义占据与 OOD 联合预测"),
            (["aerial dialog navigation"], "免训练航空视觉对话导航"),
            (["segment-centric OVSS"], "免训练开放词汇语义分割"),
            (["open-world REC"], "开放世界指代表达理解"),
            (["counterfactual UAV tracking"], "红外无人机单目标跟踪"),
            (["anchor-guided anomaly segmentation"], "零样本视觉异常分割"),
            (["VLA grounding risk"], "扩散式视觉语言动作模型的运行时失败检测"),
            (
                ["degraded missing-modality crack segmentation"],
                "任意缺失模态下的多模态裂缝分割",
            ),
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
            (["embodied navigation", "spatial memory"], "开放世界航空目标导航"),
            (["missing modality", "multimodal segmentation"], "缺失模态脑肿瘤分割"),
            (["multimodal safety", "causal intervention"], "视觉语言模型越狱诊断与无训练修复"),
            (["multimodal RAG", "anomaly detection"], "知识接地异常检测与推理"),
            (["video anomaly detection", "selective evaluation"], "弱监督视频异常检测与低误报评估"),
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
            (
                ["wildfire UAV scale detection"],
                "直接连接 UAV 微小目标与火灾弱证据",
                "尺度条件路由",
            ),
            (
                ["latent entropy decoding"],
                "词元熵不是像素不确定性",
                "滑窗熵估计",
            ),
            (
                ["saliency alignment reward"],
                "区域证据奖励",
                "框覆盖对齐奖励",
            ),
            (
                ["prototype-guided 3D OOD"],
                "已知长尾与未知 OOD 解耦",
                "EchoOOD免训练异常评分",
            ),
            (
                ["aerial dialog navigation"],
                "UAV 主动寻找弱目标",
                "Search-CoT",
            ),
            (
                ["segment-centric OVSS"],
                "区域一致推理和参考记忆",
                "区域一致交互图",
            ),
            (["open-world REC"], "类别无关候选", "结构化场景描述"),
            (
                ["counterfactual UAV tracking"],
                "背景相机运动造成的伪相关",
                "反事实运动可靠性",
            ),
            (
                ["anchor-guided anomaly segmentation"],
                "正常/异常语义锚点",
                "零样本像素异常评分",
            ),
            (
                ["VLA grounding risk"],
                "删除模型声称依赖的证据",
                "功能型 conformal 报警",
            ),
            (
                ["degraded missing-modality crack segmentation"],
                "退化模拟",
                "轻量 Needle RWKV",
            ),
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
            (
                ["embodied navigation", "spatial memory"],
                "持续搜索",
                "自适应八叉树近远场记忆",
            ),
            (
                ["missing modality", "multimodal segmentation"],
                "融合前先学稳健共享表示",
                "统一编码器遮蔽预训练",
            ),
            (
                ["multimodal safety", "causal intervention"],
                "层/路径干预诊断",
                "层阻断与 FFN/MHSA 路径干预",
            ),
            (
                ["multimodal RAG", "anomaly detection"],
                "可追溯的背景/缺陷检索文档",
                "查询到知识的多模态 RAG",
            ),
            (
                ["video anomaly detection", "selective evaluation"],
                "固定误报预算",
                "时间聚类覆盖",
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

    def test_specialized_notes_do_not_inherit_unrelated_generic_templates(self):
        cases = [
            (
                ["embodied navigation", "spatial memory", "open-world"],
                ["未探索前沿", "类别无关候选发现"],
            ),
            (
                ["video anomaly detection", "selective evaluation"],
                ["开放词汇异常识别", "区域文本对齐", "困难负例数量"],
            ),
            (
                ["multimodal safety", "causal intervention", "VLM/MLLM"],
                ["因果中介定位", "候选 mask 生成"],
            ),
        ]

        for tags, forbidden_phrases in cases:
            with self.subTest(tags=tags):
                paper = update_papers.Paper(
                    title="Specialized Paper",
                    url="https://example.com/specialized",
                    tags=tags,
                )
                note = " ".join(
                    [
                        update_papers.task_setting(paper),
                        update_papers.relation_to_topic(paper),
                        update_papers.borrow_points(paper),
                        update_papers.improvement_ideas(paper),
                    ]
                )
                for phrase in forbidden_phrases:
                    self.assertNotIn(phrase, note)


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

    def test_repeated_paper_is_expanded_once_and_cross_referenced(self):
        paper = update_papers.Paper(
            title="Shared Candidate",
            url="https://example.com/shared",
            source="CVPR 2026",
            tags=["COD", "UAV/small-object"],
        )
        item = update_papers.paper_to_dict(paper)
        snapshot = {
            "date": "2026-08-24",
            "generated_at": "2026-08-24 09:00",
            "total_selected": 1,
            "sections": {
                "highlights": [],
                "quality": [item],
                "cod": [item],
                "uav": [item],
                "fire_multispectral": [],
                "fire_foundation": [],
                "broad": [],
            },
        }

        markdown = update_papers.render_snapshot_markdown(snapshot)

        self.assertEqual(markdown.count("- 核心机制："), 1)
        self.assertEqual(markdown.count("此处仅保留方向归属"), 2)
        self.assertIn("已在“高质量来源优先读”列出", markdown)

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

    def test_update_history_excludes_papers_seen_in_non_highlight_sections(self):
        previous = self.make_paper("Previously Surfaced UAV Paper", 999, "previous-uav")
        candidates = [
            previous,
            *[
                self.make_paper(f"Fresh Paper {index}", 100 - index, f"fresh-{index}")
                for index in range(1, 6)
            ],
        ]
        old_snapshot = {
            "date": "2026-07-12",
            "generated_at": "2026-07-12 09:10",
            "sections": {
                "highlights": [],
                "uav": [update_papers.paper_to_dict(previous)],
            },
        }

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
