import sqlite3
from os.path import exists

class SQLite:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.curs = self.conn.cursor()
        if path == ":memory:" or not exists(path):
            with self.conn:
                self.curs.execute("""CREATE TABLE tours (
                    title text,
                    path text,
                    distance real,
                    type text,
                    date int
                )""")

    def add_tour(self, title, path, distance, type, date):
        with self.conn:
            self.curs.execute("INSERT INTO tours VALUES (:title, :path, :distance, :type, :date)",
                {"title": title, "path": path, "distance": distance, "type": type, "date": date})

    def print_tours(self):
        with self.conn:
            self.curs.execute("SELECT * FROM tours")
            print(self.curs.fetchall())

