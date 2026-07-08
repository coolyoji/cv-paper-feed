#!/usr/bin/env python3
"""Move already downloaded daily PDFs into Zotero via the local importer plugin."""

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


def main() -> None:
    mod = load_update_module()
    index = mod.load_download_index()
    by_date: dict[str, list[dict]] = {}
    for record in index.values():
        if not isinstance(record, dict):
            continue
        date_text = record.get("date")
        if not date_text:
            continue
        by_date.setdefault(date_text, []).append(record)

    moved_any = False
    for date_text in sorted(by_date):
        records = by_date[date_text]
        if mod.import_daily_pdfs_to_zotero(date_text, records):
            moved_any = True
            mod.save_download_index(index)
    if moved_any:
        mod.save_download_index(index)
        print("Imported existing PDFs into Zotero.")
    else:
        print("No pending PDFs were imported. Is Zotero running with the importer plugin loaded?")


if __name__ == "__main__":
    main()
