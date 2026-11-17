
import requests
from pathlib import Path

BASE_URL = "https://habr.com/ru/articles/1105688/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

Path("tests/fixtures").mkdir(parents=True, exist_ok=True)

pages = {
    "habr_article.html": BASE_URL,
    "habr_comments.html": BASE_URL + "comments"
}

for filename, url in pages.items():
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    path = Path("tests/fixtures") / filename
    path.write_text(response.text, encoding="utf-8")

    print(f"{filename} сохранён!")
    print(f"Размер HTML: {len(response.text)}")
    print()
