from src.database import DatabaseRepository

db = DatabaseRepository("test.db")

comments = db.connection.execute(
    "SELECT id, name, message FROM comments ORDER BY id"
).fetchall()

for comment in comments:
    print(f"ID: {comment['id']}")
    print(f"Имя: {comment['name']}")
    print(f"Комментарий: {comment['message']}")
    print("-" * 60)

db.close()