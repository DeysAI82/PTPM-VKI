import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS triangles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                a TEXT,
                b TEXT,
                c TEXT,
                triangle_type TEXT,
                error_message TEXT
            )
        """)
        self.connection.commit()

    def add(self, a, b, c, triangle_type, error_message):
        self.connection.execute("""
            INSERT INTO triangles
            (a, b, c, triangle_type, error_message)
            VALUES (?, ?, ?, ?, ?)
        """, (a, b, c, triangle_type, error_message))
        self.connection.commit()

    def get(self, a, b, c):
        cursor = self.connection.execute("""
            SELECT triangle_type, error_message
            FROM triangles
            WHERE a = ? AND b = ? AND c = ?
        """, (a, b, c))

        return cursor.fetchone()

    def delete(self, a, b, c):
        self.connection.execute("""
            DELETE FROM triangles
            WHERE a = ? AND b = ? AND c = ?
        """, (a, b, c))
        self.connection.commit()

    def close(self):
        self.connection.close()