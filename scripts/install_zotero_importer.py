#!/usr/bin/env python3
"""Build the local Zotero importer plugin XPI.

Install the generated XPI once from Zotero:
Tools -> Add-ons -> gear icon -> Install Add-on From File...
"""

from __future__ import annotations

import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "zotero" / "cv-paper-feed-importer"
DIST = ROOT / "dist"
ADDON_ID = "cv-paper-feed-importer@local"
XPI_NAME = f"{ADDON_ID}.xpi"


def build_xpi() -> Path:
    DIST.mkdir(parents=True, exist_ok=True)
    xpi_path = DIST / XPI_NAME
    with zipfile.ZipFile(xpi_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in PLUGIN_DIR.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(PLUGIN_DIR).as_posix())
    return xpi_path


def main() -> None:
    xpi_path = build_xpi()
    print(f"Built: {xpi_path}")
    print("Install it once from Zotero: Tools -> Add-ons -> gear icon -> Install Add-on From File...")
    print("Then restart Zotero once to load the importer endpoint.")


if __name__ == "__main__":
    main()
