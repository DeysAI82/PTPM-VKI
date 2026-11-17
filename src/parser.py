import requests
from bs4 import BeautifulSoup


class ForumParser:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def parse_page(self, url: str):
        response = requests.get(
            url,
            headers=self.headers,
            timeout=20
        )
        response.raise_for_status()

        return self.parse_html(response.text)

    def parse_html(self, html: str):
        soup = BeautifulSoup(html, "lxml")

        comments = []

        for comment in soup.find_all(
            "article",
            class_="tm-comment-thread__comment"
        ):
            comment_id = comment.get("id")

            username = comment.find(
                "a",
                class_="tm-user-info__username"
            )

            message = comment.find(
                "div",
                class_="tm-comment__body-content"
            )

            if comment_id and username and message:
                comments.append({
                    "id": int(comment_id),
                    "name": username.text.strip(),
                    "message": message.decode_contents().strip()
                })

        return comments

    def save_to_db(self, parsed_data, repository):
        count = 0

        for comment in parsed_data:
            if repository.get_by_id(comment["id"]) is None:
                repository.add(
                    comment["id"],
                    comment["name"],
                    comment["message"]
                )
                count += 1

        return count
