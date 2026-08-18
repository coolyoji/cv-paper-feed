#!/usr/bin/env python3
"""Import daily deep-reading PDFs into Zotero storage.

This is a local fallback for Zotero 7, whose localhost API is read-only.
It only writes after Zotero has been closed and a database backup has been
created.
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import re
import shutil
import sqlite3
import subprocess
import time
from pathlib import Path


LIBRARY_ID = 1
KEY_CHARS = "23456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
ZOTERO_EXE = Path(os.environ.get("ZOTERO_EXE", r"C:\Program Files\Zotero\zotero.exe"))


def detect_zotero_dir() -> Path:
    override = os.environ.get("ZOTERO_DATA_DIR")
    if override:
        return Path(override)

    if os.name == "nt":
        profile_root = (
            Path(os.environ.get("APPDATA", ""))
            / "Zotero"
            / "Zotero"
            / "Profiles"
        )
        if profile_root.exists():
            for prefs_path in sorted(profile_root.glob("*/prefs.js")):
                text = prefs_path.read_text(encoding="utf-8", errors="ignore")
                if '"extensions.zotero.useDataDir", true' not in text:
                    continue
                match = re.search(
                    r'user_pref\("extensions\.zotero\.dataDir",\s*"((?:\\.|[^"])*)"\);',
                    text,
                )
                if not match:
                    continue
                try:
                    data_dir = Path(json.loads(f'"{match.group(1)}"'))
                except json.JSONDecodeError:
                    continue
                if data_dir.exists():
                    return data_dir

    return Path.home() / "Zotero"


ZOTERO_DIR = detect_zotero_dir()


def norm_title(text: str) -> str:
    return re.sub(r"\W+", "", (text or "").lower())


def now_sql() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def safe_filename(text: str, max_chars: int = 118) -> str:
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", text or "paper")
    text = re.sub(r"\s+", " ", text).strip(" .") or "paper"
    if len(text) > max_chars:
        text = text[:max_chars].rstrip(" .")
    return text + ".pdf"


def zotero_running() -> bool:
    if os.name != "nt":
        return False
    result = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq zotero.exe", "/FO", "CSV"],
        check=False,
        capture_output=True,
        text=True,
    )
    return "zotero.exe" in result.stdout.lower()


def close_zotero(timeout_seconds: int = 30) -> bool:
    if os.name != "nt" or not zotero_running():
        return True
    script = rf"""
$procs = Get-Process -Name zotero -ErrorAction SilentlyContinue
foreach ($p in $procs) {{
  if ($p.MainWindowHandle -ne 0) {{ [void]$p.CloseMainWindow() }}
}}
$deadline = (Get-Date).AddSeconds({timeout_seconds})
while ((Get-Process -Name zotero -ErrorAction SilentlyContinue) -and (Get-Date) -lt $deadline) {{
  Start-Sleep -Milliseconds 500
}}
if (Get-Process -Name zotero -ErrorAction SilentlyContinue) {{ exit 2 }}
"""
    result = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
        check=False,
    )
    return result.returncode == 0


def restart_zotero_if_needed(was_running: bool) -> None:
    if was_running and os.name == "nt" and ZOTERO_EXE.exists():
        subprocess.Popen([str(ZOTERO_EXE)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def backup_database(zotero_dir: Path) -> Path:
    backup_dir = zotero_dir / f"backup-cv-paper-feed-{time.strftime('%Y%m%d-%H%M%S')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    for name in ["zotero.sqlite", "zotero.sqlite-wal", "zotero.sqlite-shm"]:
        path = zotero_dir / name
        if path.exists():
            shutil.copy2(path, backup_dir / name)
    return backup_dir


def make_key(cur: sqlite3.Cursor) -> str:
    while True:
        key = "".join(random.choice(KEY_CHARS) for _ in range(8))
        cur.execute("SELECT 1 FROM items WHERE libraryID=? AND key=?", (LIBRARY_ID, key))
        if cur.fetchone():
            continue
        cur.execute("SELECT 1 FROM collections WHERE libraryID=? AND key=?", (LIBRARY_ID, key))
        if cur.fetchone():
            continue
        return key


def get_ids(cur: sqlite3.Cursor) -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    cur.execute("SELECT typeName,itemTypeID FROM itemTypes")
    item_types = dict(cur.fetchall())
    cur.execute("SELECT fieldName,fieldID FROM fields")
    fields = dict(cur.fetchall())
    cur.execute("SELECT creatorType,creatorTypeID FROM creatorTypes")
    creator_types = dict(cur.fetchall())
    return item_types, fields, creator_types


def get_value_id(cur: sqlite3.Cursor, value: str | None) -> int | None:
    if not value:
        return None
    cur.execute("SELECT valueID FROM itemDataValues WHERE value=?", (value,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO itemDataValues(value) VALUES (?)", (value,))
    return cur.lastrowid


def set_field(cur: sqlite3.Cursor, item_id: int, field_id: int, value: str | None) -> None:
    value_id = get_value_id(cur, value)
    if value_id is None:
        return
    cur.execute(
        "INSERT OR REPLACE INTO itemData(itemID,fieldID,valueID) VALUES (?,?,?)",
        (item_id, field_id, value_id),
    )


def get_or_create_collection(cur: sqlite3.Cursor, name: str, parent_id: int | None) -> int:
    cur.execute(
        """SELECT c.collectionID FROM collections c
           LEFT JOIN deletedCollections d ON d.collectionID=c.collectionID
           WHERE c.libraryID=? AND c.collectionName=?
           AND d.collectionID IS NULL
           AND ((c.parentCollectionID IS NULL AND ? IS NULL) OR c.parentCollectionID=?)
           ORDER BY c.collectionID DESC
           LIMIT 1""",
        (LIBRARY_ID, name, parent_id, parent_id),
    )
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute(
        """INSERT INTO collections(collectionName,parentCollectionID,clientDateModified,libraryID,key,version,synced)
           VALUES (?,?,?,?,?,?,?)""",
        (name, parent_id, now_sql(), LIBRARY_ID, make_key(cur), 0, 0),
    )
    return cur.lastrowid


def daily_collection(cur: sqlite3.Cursor, date_text: str, root_name: str) -> tuple[int, str]:
    year, month, day = date_text.split("-")
    root = get_or_create_collection(cur, root_name, None)
    year_id = get_or_create_collection(cur, year, root)
    month_id = get_or_create_collection(cur, month, year_id)
    day_id = get_or_create_collection(cur, day, month_id)
    return day_id, f"{root_name}/{year}/{month}/{day}"


def build_title_index(cur: sqlite3.Cursor, fields: dict[str, int]) -> dict[str, int]:
    cur.execute(
        """SELECT i.itemID, v.value
           FROM items i
           JOIN itemData d ON d.itemID=i.itemID AND d.fieldID=?
           JOIN itemDataValues v ON v.valueID=d.valueID
           LEFT JOIN deletedItems deleted ON deleted.itemID=i.itemID
           WHERE i.libraryID=? AND deleted.itemID IS NULL
             AND i.itemTypeID != (
               SELECT itemTypeID FROM itemTypes WHERE typeName='attachment'
             )""",
        (fields["title"], LIBRARY_ID),
    )
    return {norm_title(title): item_id for item_id, title in cur.fetchall() if norm_title(title)}


def mark_item_unsynced(cur: sqlite3.Cursor, item_id: int) -> None:
    cur.execute(
        "UPDATE items SET clientDateModified=?, synced=0 WHERE itemID=?",
        (now_sql(), item_id),
    )


def remove_tombstoned_sibling_memberships(
    cur: sqlite3.Cursor, collection_id: int, item_id: int
) -> bool:
    cur.execute(
        """DELETE FROM collectionItems
           WHERE itemID=? AND collectionID IN (
             SELECT old.collectionID
             FROM collections active
             JOIN collections old
               ON old.libraryID=active.libraryID
              AND old.collectionName=active.collectionName
              AND (
                (old.parentCollectionID IS NULL AND active.parentCollectionID IS NULL)
                OR old.parentCollectionID=active.parentCollectionID
              )
             JOIN deletedCollections d ON d.collectionID=old.collectionID
             WHERE active.collectionID=? AND old.collectionID!=active.collectionID
           )""",
        (item_id, collection_id),
    )
    if cur.rowcount <= 0:
        return False
    mark_item_unsynced(cur, item_id)
    return True


def add_to_collection(cur: sqlite3.Cursor, collection_id: int, item_id: int) -> bool:
    cur.execute(
        "SELECT 1 FROM collectionItems WHERE collectionID=? AND itemID=?",
        (collection_id, item_id),
    )
    if cur.fetchone():
        return False
    cur.execute(
        "SELECT COALESCE(MAX(orderIndex), -1) + 1 FROM collectionItems WHERE collectionID=?",
        (collection_id,),
    )
    cur.execute(
        "INSERT INTO collectionItems(collectionID,itemID,orderIndex) VALUES (?,?,?)",
        (collection_id, item_id, cur.fetchone()[0]),
    )
    mark_item_unsynced(cur, item_id)
    return True


def split_name(name: str) -> tuple[str, str, int] | None:
    name = (name or "").strip()
    if not name:
        return None
    if "," in name:
        last, first = name.split(",", 1)
        return first.strip(), last.strip(), 0
    parts = name.split()
    if len(parts) == 1:
        return "", name, 1
    return " ".join(parts[:-1]), parts[-1], 0


def item_type_for(record: dict) -> str:
    source = (record.get("source") or "").lower()
    url = (record.get("url") or record.get("pdf") or "").lower()
    if "arxiv" in source or "arxiv.org" in url:
        return "preprint"
    if any(venue in source for venue in ["cvpr", "iccv", "eccv", "wacv"]):
        return "conferencePaper"
    return "journalArticle"


def create_item(cur: sqlite3.Cursor, item_type_name: str, item_types: dict[str, int]) -> tuple[int, str]:
    key = make_key(cur)
    timestamp = now_sql()
    cur.execute(
        """INSERT INTO items(itemTypeID,dateAdded,dateModified,clientDateModified,libraryID,key,version,synced)
           VALUES (?,?,?,?,?,?,?,?)""",
        (item_types[item_type_name], timestamp, timestamp, timestamp, LIBRARY_ID, key, 0, 0),
    )
    return cur.lastrowid, key


def add_creators(cur: sqlite3.Cursor, item_id: int, authors: list[str], creator_type_id: int) -> None:
    for order, raw_name in enumerate(authors):
        parsed = split_name(raw_name)
        if not parsed:
            continue
        first, last, mode = parsed
        cur.execute(
            "SELECT creatorID FROM creators WHERE lastName=? AND firstName=? AND fieldMode=?",
            (last, first, mode),
        )
        row = cur.fetchone()
        if row:
            creator_id = row[0]
        else:
            cur.execute(
                "INSERT INTO creators(firstName,lastName,fieldMode) VALUES (?,?,?)",
                (first, last, mode),
            )
            creator_id = cur.lastrowid
        cur.execute(
            """INSERT OR IGNORE INTO itemCreators(itemID,creatorID,creatorTypeID,orderIndex)
               VALUES (?,?,?,?)""",
            (item_id, creator_id, creator_type_id, order),
        )


def add_tags(cur: sqlite3.Cursor, item_id: int, tags: list[str]) -> None:
    for tag in tags:
        tag = str(tag).strip()
        if not tag:
            continue
        cur.execute("SELECT tagID FROM tags WHERE name=?", (tag,))
        row = cur.fetchone()
        if row:
            tag_id = row[0]
        else:
            cur.execute("INSERT INTO tags(name) VALUES (?)", (tag,))
            tag_id = cur.lastrowid
        cur.execute(
            "INSERT OR IGNORE INTO itemTags(itemID,tagID,type) VALUES (?,?,?)",
            (item_id, tag_id, 0),
        )


def create_parent_item(
    cur: sqlite3.Cursor,
    record: dict,
    item_types: dict[str, int],
    fields: dict[str, int],
    creator_types: dict[str, int],
) -> int:
    item_type = item_type_for(record)
    item_id, _ = create_item(cur, item_type, item_types)
    set_field(cur, item_id, fields["title"], record.get("title") or "Untitled")
    set_field(cur, item_id, fields["abstractNote"], record.get("summary"))
    set_field(cur, item_id, fields["date"], record.get("published"))
    set_field(cur, item_id, fields["url"], record.get("url"))
    set_field(cur, item_id, fields["libraryCatalog"], "cv-paper-feed")
    source_field = "proceedingsTitle" if item_type == "conferencePaper" else "publicationTitle"
    set_field(cur, item_id, fields[source_field], record.get("source"))
    extra = [f"Daily deep read date: {record.get('date', '')}"]
    if record.get("pdf"):
        extra.append(f"Original PDF: {record.get('pdf')}")
    set_field(cur, item_id, fields["extra"], "\n".join(extra))
    add_creators(cur, item_id, record.get("authors") or [], creator_types["author"])
    add_tags(cur, item_id, ["daily-deep-read", "cv-paper-feed"] + list(record.get("tags") or []))
    return item_id


def parent_has_attachment(cur: sqlite3.Cursor, parent_id: int) -> bool:
    cur.execute("SELECT itemID FROM itemAttachments WHERE parentItemID=? LIMIT 1", (parent_id,))
    return cur.fetchone() is not None


def create_attachment(
    cur: sqlite3.Cursor,
    parent_id: int,
    pdf_path: Path,
    item_types: dict[str, int],
    fields: dict[str, int],
    storage_dir: Path,
) -> Path:
    attachment_id, attachment_key = create_item(cur, "attachment", item_types)
    destination_dir = storage_dir / attachment_key
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / safe_filename(pdf_path.stem)
    suffix = 1
    while destination.exists():
        destination = destination_dir / f"{destination.stem[:100]}-{suffix}.pdf"
        suffix += 1
    shutil.copy2(pdf_path, destination)
    stat = destination.stat()
    md5 = hashlib.md5(destination.read_bytes()).hexdigest()
    cur.execute(
        """INSERT INTO itemAttachments(
              itemID,parentItemID,linkMode,contentType,charsetID,path,syncState,storageModTime,storageHash,
              lastProcessedModificationTime,lastRead
           ) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        (
            attachment_id,
            parent_id,
            0,
            "application/pdf",
            None,
            "storage:" + destination.name,
            2,
            int(stat.st_mtime * 1000),
            md5,
            None,
            None,
        ),
    )
    set_field(cur, attachment_id, fields["title"], "PDF")
    cur.execute(
        """INSERT OR IGNORE INTO fulltextItems(
              itemID,indexedPages,totalPages,indexedChars,totalChars,version,synced
           ) VALUES (?,?,?,?,?,?,?)""",
        (attachment_id, None, None, None, None, 0, 2),
    )
    return destination


def import_records_to_zotero(
    date_text: str,
    records: list[dict],
    root_collection: str = "每日精读论文",
    close_running: bool = True,
    repair_existing: bool = False,
) -> bool:
    pending = [
        record
        for record in records
        if not record.get("zotero_imported")
        and record.get("file")
        and Path(record["file"]).exists()
    ]
    imported_records = (
        [
            record
            for record in records
            if record.get("zotero_imported") and record.get("zotero_item_id")
        ]
        if repair_existing
        else []
    )
    if not pending and not imported_records:
        return False

    was_running = zotero_running()
    if was_running:
        if not close_running or not close_zotero():
            print("[warn] Zotero is running and could not be closed; keeping F-drive PDFs.")
            return False

    db_path = ZOTERO_DIR / "zotero.sqlite"
    storage_dir = ZOTERO_DIR / "storage"
    backup_dir = backup_database(ZOTERO_DIR)
    copied_paths: list[Path] = []

    con: sqlite3.Connection | None = None
    try:
        con = sqlite3.connect(db_path)
        con.execute("PRAGMA foreign_keys=ON")
        cur = con.cursor()
        item_types, fields, creator_types = get_ids(cur)
        title_index = build_title_index(cur, fields)
        cur.execute("BEGIN")
        collection_id, collection_path = daily_collection(cur, date_text, root_collection)

        relinked = 0
        for record in imported_records:
            parent_id = int(record["zotero_item_id"])
            title_key = norm_title(record.get("title", ""))
            cur.execute(
                """SELECT v.value FROM items i
                   JOIN itemData data ON data.itemID=i.itemID AND data.fieldID=?
                   JOIN itemDataValues v ON v.valueID=data.valueID
                   LEFT JOIN deletedItems deleted ON deleted.itemID=i.itemID
                   WHERE i.itemID=? AND i.libraryID=? AND deleted.itemID IS NULL""",
                (fields["title"], parent_id, LIBRARY_ID),
            )
            row = cur.fetchone()
            if not row or (title_key and norm_title(row[0]) != title_key):
                parent_id = title_index.get(title_key)
            if parent_id is None:
                continue
            remove_tombstoned_sibling_memberships(cur, collection_id, parent_id)
            add_to_collection(cur, collection_id, parent_id)
            record["zotero_collection_path"] = collection_path
            relinked += 1

        for record in pending:
            title_key = norm_title(record.get("title", ""))
            parent_id = title_index.get(title_key)
            if parent_id is None:
                parent_id = create_parent_item(cur, record, item_types, fields, creator_types)
                title_index[title_key] = parent_id
            remove_tombstoned_sibling_memberships(cur, collection_id, parent_id)
            add_to_collection(cur, collection_id, parent_id)

            pdf_path = Path(record["file"])
            if pdf_path.exists() and not parent_has_attachment(cur, parent_id):
                copied_paths.append(
                    create_attachment(cur, parent_id, pdf_path, item_types, fields, storage_dir)
                )

            record["zotero_imported"] = True
            record["zotero_item_id"] = parent_id
            record["zotero_collection_path"] = collection_path
            record["zotero_imported_at"] = time.strftime("%Y-%m-%d %H:%M")

        con.commit()
    except Exception:
        try:
            if con is not None:
                con.rollback()
        except Exception:
            pass
        for path in copied_paths:
            shutil.rmtree(path.parent, ignore_errors=True)
        print(f"[warn] Zotero import failed; database backup is at {backup_dir}")
        raise
    finally:
        try:
            if con is not None:
                con.close()
        except Exception:
            pass
        restart_zotero_if_needed(was_running)

    removed = 0
    for record in pending:
        pdf_path = Path(record.get("file", ""))
        if pdf_path.exists() and record.get("zotero_imported"):
            pdf_path.unlink()
            record["local_pdf_moved_to_zotero"] = True
            removed += 1
    if pending:
        print(
            f"[info] imported {len(pending)} PDFs into Zotero collection "
            f"{root_collection}/{date_text.replace('-', '/')}; "
            f"removed {removed} F-drive PDFs"
        )
    if imported_records:
        print(
            f"[info] ensured {relinked} existing Zotero items remain linked to "
            f"{root_collection}/{date_text.replace('-', '/')}"
        )
    return True


if __name__ == "__main__":
    root = Path(os.environ.get("PAPER_DOWNLOAD_ROOT", r"F:\文献整理\每日精读论文"))
    index_path = root / "_downloaded_papers.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    by_date: dict[str, list[dict]] = {}
    for record in index.values():
        if isinstance(record, dict) and record.get("date"):
            by_date.setdefault(record["date"], []).append(record)
    changed = False
    for day, records_for_day in sorted(by_date.items()):
        changed = import_records_to_zotero(day, records_for_day) or changed
    if changed:
        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2),
            encoding="utf-8",
            newline="\n",
        )
