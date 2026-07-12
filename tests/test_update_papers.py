import importlib.util
import sys
import unittest
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "update_papers.py"
SPEC = importlib.util.spec_from_file_location("update_papers", MODULE_PATH)
update_papers = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = update_papers
SPEC.loader.exec_module(update_papers)


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

        self.assertIn("## 多光谱火灾探测", markdown)
        self.assertIn("## 火灾监测大模型", markdown)
        self.assertIn("WildFireVLM", markdown)

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
        self.assertNotIn("## 多光谱火灾探测", markdown)
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


if __name__ == "__main__":
    unittest.main()
