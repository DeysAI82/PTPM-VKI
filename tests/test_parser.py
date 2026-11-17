import unittest
from pathlib import Path

from src.parser import ForumParser
from src.database import DatabaseRepository


class TestForumParser(unittest.TestCase):

    def setUp(self):
        self.parser = ForumParser()

        path = Path("tests/fixtures/habr_comments.html")
        self.html = path.read_text(encoding="utf-8")

        self.db = DatabaseRepository(":memory:")

    def tearDown(self):
        self.db.close()

    def test_parse_html(self):
        result = self.parser.parse_html(self.html)

        self.assertEqual(len(result), 25)
        self.assertEqual(result[0]["id"], 30620692)
        self.assertEqual(result[0]["name"], "vladislav_smirnov")
        self.assertIn("Красивое", result[0]["message"])

    def test_save_to_db(self):
        parsed_data = self.parser.parse_html(self.html)

        count = self.parser.save_to_db(
            parsed_data,
            self.db
        )

        self.assertEqual(count, 25)
        self.assertEqual(
            self.db.get_by_id(30620692)["name"],
            "vladislav_smirnov"
        )


if __name__ == "__main__":
    unittest.main()
