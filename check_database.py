from triangle_database import Database

database = Database()

database.add(3, 4, 5, "разносторонний", "")
print(database.get(3, 4, 5))

database.delete(3, 4, 5)
print(database.get(3, 4, 5))

database.close()