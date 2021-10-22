from datetime import datetime
from os import write
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
import json
import gpx

#print(gpx.get_distance("gpx/test_run.gpx"))
#print(gpx.get_elevation("gpx/test_run.gpx"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'

db = SQLAlchemy(app)
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    path = db.Column(db.String(255))

@app.route("/")
def index():
    return "Hello World"

@app.route("/api", methods=['POST'])
def api_page():
    title =  request.files['title'].read().decode('utf-8')
    date = request.files['date'].read().decode('utf-8')
    file = request.files['file'].read().decode('utf-8')
    with open('./gpx/' + title + date, 'w') as file1:
        file1.write(file)
    Tour(title=title, date=date)
    print("Title: "+ title)
    print("Date: "+ date)
    print(file)
    return "recieved"

if __name__ == "__main__":
    app.run(port = 1337, debug=True)