import unittest
import sqlite3

from src.database import DatabaseRepository


class TestDatabaseRepository(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseRepository(":memory:")

    def tearDown(self):
        self.db.close()

    def test_add(self):
        result = self.db.add(1, "user1", "Привет!")
        self.assertTrue(result)

    def test_add_duplicate(self):
        self.db.add(1, "user1", "Привет!")

        with self.assertRaises(sqlite3.IntegrityError):
            self.db.add(1, "user2", "Другой текст")

    def test_get_by_id(self):
        self.db.add(1, "user1", "Привет!")
        result = self.db.get_by_id(1)

        self.assertEqual(result["name"], "user1")

    def test_get_by_id_not_found(self):
        result = self.db.get_by_id(100)
        self.assertIsNone(result)

    def test_get_by_name(self):
        self.db.add(1, "user1", "Первое сообщение")
        self.db.add(2, "user1", "Второе сообщение")

        result = self.db.get_by_name("user1")

        self.assertEqual(len(result), 2)

    def test_get_by_name_empty(self):
        result = self.db.get_by_name("unknown")
        self.assertEqual(result, [])

    def test_update(self):
        self.db.add(1, "user1", "Старый текст")

        result = self.db.update(1, "Новый текст")

        self.assertTrue(result)
        self.assertEqual(
            self.db.get_by_id(1)["message"],
            "Новый текст"
        )

    def test_update_not_found(self):
        result = self.db.update(100, "Новый текст")
        self.assertFalse(result)

    def test_delete(self):
        self.db.add(1, "user1", "Привет!")

        result = self.db.delete(1)

        self.assertTrue(result)
        self.assertIsNone(self.db.get_by_id(1))

    def test_delete_not_found(self):
        result = self.db.delete(100)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()