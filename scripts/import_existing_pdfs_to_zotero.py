#!/usr/bin/env python3
"""Move already downloaded daily PDFs into Zotero storage."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPDATE_SCRIPT = ROOT / "scripts" / "update_papers.py"


def load_update_module():
    spec = importlib.util.spec_from_file_location("update_papers", UPDATE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {UPDATE_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def pending_records_by_date(index: dict) -> dict[str, list[dict]]:
    by_date: dict[str, list[dict]] = {}
    for record in index.values():
        if not isinstance(record, dict) or record.get("zotero_imported"):
            continue
        date_text = record.get("date")
        file_text = record.get("file")
        if not date_text or not file_text or not Path(file_text).exists():
            continue
        by_date.setdefault(date_text, []).append(record)
    return by_date


def write_import_receipt(root: Path, date_text: str, records: list[dict]) -> None:
    year, month, day = date_text.split("-")
    folder = root / year / month / day
    if not folder.exists():
        return
    collection = f"每日精读论文/{year}/{month}/{day}"
    lines = [
        f"# {date_text} 每日精读论文 PDF",
        "",
        f"Zotero collection: {collection}",
        "PDF cache: cleared after successful import",
        "",
        "## 已导入",
        "",
    ]
    for record in records:
        lines.extend(
            [
                f"- **{record.get('title', 'Untitled')}**",
                f"  - Zotero item ID: {record.get('zotero_item_id', '')}",
                f"  - Source: {record.get('source', '')}",
                "",
            ]
        )
    (folder / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    mod = load_update_module()
    index = mod.load_download_index()
    by_date = pending_records_by_date(index)

    moved_any = False
    for date_text in sorted(by_date):
        records = by_date[date_text]
        if mod.import_daily_pdfs_to_zotero(date_text, records):
            moved_any = True
            mod.save_download_index(index)
            write_import_receipt(mod.DOWNLOAD_ROOT, date_text, records)
    if moved_any:
        mod.save_download_index(index)
        print("Imported existing PDFs into Zotero.")
    else:
        print("No pending PDFs were imported. Check whether the PDFs still exist or Zotero could be closed.")


if __name__ == "__main__":
    main()
