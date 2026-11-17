import sqlite3


class DatabaseRepository:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def add(self, comment_id: int, username: str, message: str):
        if not isinstance(comment_id, int) or isinstance(comment_id, bool):
            raise TypeError("ID должен быть целым числом")

        if not isinstance(username, str):
            raise TypeError("Имя должно быть строкой")

        if not isinstance(message, str):
            raise TypeError("Сообщение должно быть строкой")

        if len(username) > 256:
            raise ValueError("Имя не должно превышать 256 символов")

        if len(message) > 8096:
            raise ValueError("Сообщение не должно превышать 8096 символов")

        self.connection.execute(
            "INSERT INTO comments (id, name, message) VALUES (?, ?, ?)",
            (comment_id, username, message)
        )
        self.connection.commit()

        return True

    def get_by_id(self, comment_id: int):
        cursor = self.connection.execute(
            "SELECT * FROM comments WHERE id = ?",
            (comment_id,)
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return dict(result)

    def get_by_name(self, username: str):
        cursor = self.connection.execute(
            "SELECT * FROM comments WHERE name = ?",
            (username,)
        )

        return [dict(row) for row in cursor.fetchall()]

    def update(self, comment_id: int, new_message: str):
        if not isinstance(new_message, str):
            raise TypeError("Сообщение должно быть строкой")

        if len(new_message) > 8096:
            raise ValueError("Сообщение не должно превышать 8096 символов")

        cursor = self.connection.execute(
            "UPDATE comments SET message = ? WHERE id = ?",
            (new_message, comment_id)
        )
        self.connection.commit()

        return cursor.rowcount > 0

    def delete(self, comment_id: int):
        cursor = self.connection.execute(
            "DELETE FROM comments WHERE id = ?",
            (comment_id,)
        )
        self.connection.commit()

        return cursor.rowcount > 0

    def close(self):
        self.connection.close()