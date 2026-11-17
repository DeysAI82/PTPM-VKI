import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/articles/1105688/comments"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

comments = soup.find_all(
    "article",
    class_="tm-comment-thread__comment"
)

print("Найдено комментариев:", len(comments))
print("-" * 60)

for comment in comments:
    comment_id = comment.get("id")

    username = comment.find(
        "a",
        class_="tm-user-info__username"
    )

    message = comment.find(
        "div",
        class_="tm-comment__body-content"
    )

    if username and message:
        print("ID:", comment_id)
        print("Имя:", username.text.strip())
        print("Комментарий:", message.get_text(" ", strip=True))
        print("-" * 60)