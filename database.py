import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/olist.db")


def create_database():
    connection = sqlite3.connect(DATABASE_PATH)

    with open("schema.sql", "r") as file:
        schema = file.read()

    connection.executescript(schema)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")