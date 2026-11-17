
from pathlib import Path

from src.parser import ForumParser
from src.database import DatabaseRepository


parser = ForumParser()
repository = DatabaseRepository("test.db")

html = Path(
    "tests/fixtures/habr_comments.html"
).read_text(encoding="utf-8")

parsed_data = parser.parse_html(html)

print("Найдено комментариев:", len(parsed_data))

saved_count = parser.save_to_db(
    parsed_data,
    repository
)

print("Сохранено новых комментариев:", saved_count)

print("\nПервый комментарий:")

if parsed_data:
    print(parsed_data[0])

repository.close()
