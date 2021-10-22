from datetime import datetime
import re
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
import gpx

print(gpx.get_distance("gpx/test_run.gpx"))
print(gpx.get_elevation("gpx/test_run.gpx"))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'

db = SQLAlchemy(app)
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return "Title: " + self.title


@app.route("/")
def index():
    return "Hello World"

@app.route("/api", methods=['POST'])
def api_page():
    if request.method == 'POST':
        request_data = request.get_json()
        print(request_data)
        title = request_data['title']
        date = request_data['date']
        print("Title: " + title)
        print("Date: " + date)
        return "recieved"
    else:
        return "invalid"

@app.route("/api/file", methods=['POST'])
def api_page_file():
    if request.method == 'POST':
        request_files = request.files.getlist('document')
        print(request_files)
        return "recieved"
    else:
        return "invalid"

if __name__ == "__main__":
    app.run(port = 1337, debug=True)

