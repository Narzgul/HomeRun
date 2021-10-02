import sqlite3

conn = sqlite3.connect(":memory:")
curs = conn.cursor()

def add_tour(title, path, distance, type, date):
    with conn:
        curs.execute("INSERT INTO tours VALUES (:title, :path, :distance, :type, :date)",
            {"title": title, "path": path, "distance": distance, "type": type, "date": date})

def print_tours():
    with conn:
        curs.execute("SELECT * FROM tours")
        print(curs.fetchall())

with conn:
    curs.execute("""CREATE TABLE tours (
        title text,
        path text,
        distance real,
        type text,
        date int
    )""")

add_tour("My first run", "./gpx/my_first_run.gpx", 4.95, "run", 1633105270)
print_tours()