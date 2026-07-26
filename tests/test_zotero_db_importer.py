import importlib.util
import sqlite3
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "zotero_db_importer.py"
SPEC = importlib.util.spec_from_file_location("zotero_db_importer", MODULE_PATH)
zotero_db_importer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = zotero_db_importer
SPEC.loader.exec_module(zotero_db_importer)


class CollectionRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.cur = self.con.cursor()
        self.cur.executescript(
            """
            CREATE TABLE collections (
                collectionID INTEGER PRIMARY KEY,
                collectionName TEXT NOT NULL,
                parentCollectionID INTEGER,
                clientDateModified TEXT,
                libraryID INTEGER NOT NULL,
                key TEXT NOT NULL,
                version INTEGER NOT NULL,
                synced INTEGER NOT NULL
            );
            CREATE TABLE deletedCollections (
                collectionID INTEGER PRIMARY KEY
            );
            CREATE TABLE items (
                itemID INTEGER PRIMARY KEY,
                libraryID INTEGER NOT NULL,
                key TEXT NOT NULL,
                clientDateModified TEXT,
                version INTEGER NOT NULL DEFAULT 0,
                synced INTEGER NOT NULL DEFAULT 0
            );
            CREATE TABLE collectionItems (
                collectionID INTEGER NOT NULL,
                itemID INTEGER NOT NULL,
                orderIndex INTEGER NOT NULL,
                PRIMARY KEY (collectionID, itemID)
            );
            """
        )

    def tearDown(self):
        self.con.close()

    def test_reuses_active_collection_without_changing_sync_state(self):
        self.cur.execute(
            """INSERT INTO collections
               VALUES (1, '26', NULL, '2026-07-25 01:00:00', 1, 'ABCDEFGH', 7, 1)"""
        )

        collection_id = zotero_db_importer.get_or_create_collection(
            self.cur, "26", None
        )

        self.assertEqual(collection_id, 1)
        self.cur.execute(
            "SELECT version, synced FROM collections WHERE collectionID=1"
        )
        self.assertEqual(self.cur.fetchone(), (7, 1))

    def test_replaces_tombstoned_collection_with_a_new_sync_key(self):
        self.cur.execute(
            """INSERT INTO collections
               VALUES (1, '26', NULL, '2026-07-25 01:00:00', 1, 'ABCDEFGH', 7, 1)"""
        )
        self.cur.execute("INSERT INTO deletedCollections VALUES (1)")

        collection_id = zotero_db_importer.get_or_create_collection(
            self.cur, "26", None
        )

        self.assertNotEqual(collection_id, 1)
        self.cur.execute(
            "SELECT key, version, synced FROM collections WHERE collectionID=?",
            (collection_id,),
        )
        key, version, synced = self.cur.fetchone()
        self.assertNotEqual(key, "ABCDEFGH")
        self.assertEqual((version, synced), (0, 0))
        self.cur.execute(
            "SELECT 1 FROM deletedCollections WHERE collectionID=1"
        )
        self.assertIsNotNone(self.cur.fetchone())
        self.assertEqual(
            zotero_db_importer.get_or_create_collection(self.cur, "26", None),
            collection_id,
        )

    def test_new_membership_marks_item_unsynced_but_existing_membership_does_not(self):
        self.cur.execute(
            """INSERT INTO collections
               VALUES (1, '26', NULL, '2026-07-25 01:00:00', 1, 'ABCDEFGH', 7, 1)"""
        )
        self.cur.execute(
            """INSERT INTO items
               VALUES (10, 1, 'ITEMKEY1', '2026-07-25 01:00:00', 9, 1)"""
        )

        self.assertTrue(zotero_db_importer.add_to_collection(self.cur, 1, 10))
        self.cur.execute("SELECT synced FROM items WHERE itemID=10")
        self.assertEqual(self.cur.fetchone()[0], 0)

        self.cur.execute(
            "UPDATE items SET clientDateModified='stable', synced=1 WHERE itemID=10"
        )
        self.assertFalse(zotero_db_importer.add_to_collection(self.cur, 1, 10))
        self.cur.execute(
            "SELECT clientDateModified, synced FROM items WHERE itemID=10"
        )
        self.assertEqual(self.cur.fetchone(), ("stable", 1))

    def test_migrates_membership_away_from_tombstoned_sibling(self):
        self.cur.executemany(
            """INSERT INTO collections
               VALUES (?, '26', NULL, '2026-07-25 01:00:00', 1, ?, 7, 1)""",
            [(1, "OLDKEY11"), (2, "NEWKEY22")],
        )
        self.cur.execute("INSERT INTO deletedCollections VALUES (1)")
        self.cur.execute(
            """INSERT INTO items
               VALUES (10, 1, 'ITEMKEY1', '2026-07-25 01:00:00', 9, 1)"""
        )
        self.cur.execute("INSERT INTO collectionItems VALUES (1, 10, 0)")

        self.assertTrue(
            zotero_db_importer.remove_tombstoned_sibling_memberships(
                self.cur, 2, 10
            )
        )
        self.assertTrue(zotero_db_importer.add_to_collection(self.cur, 2, 10))
        self.cur.execute(
            "SELECT collectionID FROM collectionItems WHERE itemID=10"
        )
        self.assertEqual(self.cur.fetchall(), [(2,)])
        self.cur.execute("SELECT version, synced FROM items WHERE itemID=10")
        self.assertEqual(self.cur.fetchone(), (9, 0))


if __name__ == "__main__":
    unittest.main()
