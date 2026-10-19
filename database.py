
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS deliveries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                weight REAL,
                distance INTEGER,
                package_type TEXT,
                is_express INTEGER,
                cost INTEGER,
                delivery_date TEXT
            )
        """)
        self.connection.commit()

    def add(self, weight, distance, package_type, is_express, cost, delivery_date):
        self.connection.execute("""
            INSERT INTO deliveries
            (weight, distance, package_type, is_express, cost, delivery_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (weight, distance, package_type, int(is_express), cost, delivery_date))
        self.connection.commit()

    def get(self, weight, distance, package_type, is_express):
        cursor = self.connection.execute("""
            SELECT cost, delivery_date FROM deliveries
            WHERE weight = ? AND distance = ?
            AND package_type = ? AND is_express = ?
        """, (weight, distance, package_type, int(is_express)))
        return cursor.fetchone()

    def delete(self, weight, distance, package_type, is_express):
        self.connection.execute("""
            DELETE FROM deliveries
            WHERE weight = ? AND distance = ?
            AND package_type = ? AND is_express = ?
        """, (weight, distance, package_type, int(is_express)))
        self.connection.commit()

    def close(self):
        self.connection.close()
