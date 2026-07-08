#!/usr/bin/env python3
"""Build and stage the local Zotero importer plugin for this profile."""

from __future__ import annotations

import configparser
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "zotero" / "cv-paper-feed-importer"
DIST = ROOT / "dist"
ADDON_ID = "cv-paper-feed-importer@local"
XPI_NAME = f"{ADDON_ID}.xpi"


def zotero_profile_dir() -> Path:
    profiles_ini = Path.home() / "AppData" / "Roaming" / "Zotero" / "Zotero" / "Profiles.ini"
    if not profiles_ini.exists():
        raise FileNotFoundError(f"Zotero Profiles.ini not found: {profiles_ini}")
    parser = configparser.ConfigParser()
    parser.read(profiles_ini, encoding="utf-8")
    base = profiles_ini.parent
    for section in parser.sections():
        if not section.startswith("Profile"):
            continue
        path = parser.get(section, "Path", fallback="")
        if not path:
            continue
        is_relative = parser.getboolean(section, "IsRelative", fallback=True)
        return base / path if is_relative else Path(path)
    raise RuntimeError("No Zotero profile found in Profiles.ini")


def build_xpi() -> Path:
    DIST.mkdir(parents=True, exist_ok=True)
    xpi_path = DIST / XPI_NAME
    with zipfile.ZipFile(xpi_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in PLUGIN_DIR.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(PLUGIN_DIR).as_posix())
    return xpi_path


def install_xpi(xpi_path: Path) -> Path:
    profile = zotero_profile_dir()
    extensions = profile / "extensions"
    extensions.mkdir(parents=True, exist_ok=True)
    target = extensions / XPI_NAME
    shutil.copy2(xpi_path, target)
    return target


def main() -> None:
    xpi_path = build_xpi()
    target = install_xpi(xpi_path)
    print(f"Built: {xpi_path}")
    print(f"Staged for Zotero: {target}")
    print("Restart Zotero once to load the importer endpoint.")


if __name__ == "__main__":
    main()
