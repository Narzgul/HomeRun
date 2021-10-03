import gpx
import sqlite

db = sqlite.SQLite(":memory:")
db.add_tour("My first run", "gpx/test_run.gpx", 4.95, "run", 1633105270)
db.print_tours()

print(gpx.get_distance("gpx/test_run.gpx"))
print(gpx.get_elevation("gpx/test_run.gpx"))
