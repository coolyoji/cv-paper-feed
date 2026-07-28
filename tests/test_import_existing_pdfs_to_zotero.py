import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "import_existing_pdfs_to_zotero.py"
SPEC = importlib.util.spec_from_file_location("import_existing_pdfs_to_zotero", MODULE_PATH)
import_existing = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = import_existing
SPEC.loader.exec_module(import_existing)


class PendingRecordsByDateTests(unittest.TestCase):
    def test_only_existing_unimported_pdfs_are_grouped(self):
        with tempfile.TemporaryDirectory() as tmp:
            pending_pdf = Path(tmp) / "pending.pdf"
            pending_pdf.write_bytes(b"%PDF-test")
            missing_pdf = Path(tmp) / "missing.pdf"
            index = {
                "pending": {
                    "date": "2026-07-28",
                    "file": str(pending_pdf),
                },
                "already-imported": {
                    "date": "2026-07-27",
                    "file": str(pending_pdf),
                    "zotero_imported": True,
                },
                "missing": {
                    "date": "2026-07-26",
                    "file": str(missing_pdf),
                },
            }

            grouped = import_existing.pending_records_by_date(index)

        self.assertEqual(list(grouped), ["2026-07-28"])
        self.assertEqual(grouped["2026-07-28"], [index["pending"]])

    def test_import_receipt_records_cleared_cache_and_item_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "2026" / "07" / "28"
            folder.mkdir(parents=True)
            import_existing.write_import_receipt(
                root,
                "2026-07-28",
                [{"title": "Paper A", "source": "CVPR 2026", "zotero_item_id": 42}],
            )
            receipt = (folder / "README.md").read_text(encoding="utf-8")

        self.assertIn("PDF cache: cleared after successful import", receipt)
        self.assertIn("Zotero item ID: 42", receipt)


if __name__ == "__main__":
    unittest.main()
