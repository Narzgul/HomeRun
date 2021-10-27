from datetime import datetime
from os import write
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Doesn't use the Flask-SQLAlchemy event system
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'    # Sets the DB

db = SQLAlchemy(app)
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    path = db.Column(db.String(255))    # Path to the .gpx file
    distance = db.Column(db.Integer)
    ele_pos = db.Column(db.Integer) # Positive elevation (=up)
    ele_neg = db.Column(db.Integer) # Negative elevation (=down)


@app.route("/")
def index():
    return "<i>*with a thicc british accent*</i>: Use the focking API mate!"

@app.route("/api", methods=['POST'])
def api_page():
    title =  request.files['title'].read().decode('utf-8')
    date = request.files['date'].read().decode('utf-8')
    file = request.files['file'].read().decode('utf-8')
    distance = request.files['distance'].read().decode('utf-8')
    ele_pos = request.files['ele_pos'].read().decode('utf-8')
    ele_neg = request.files['ele_neg'].read().decode('utf-8')
    with open('./gpx/' + title + date, 'w') as file1:
        file1.write(file)   # Saves the recieved file to the gpx dir
    
    Tour(title=title, date=date, distance=distance, ele_pos=ele_pos, ele_neg=ele_neg)

    print("Title: "+ title)
    print("Date: "+ date)
    return "" # Apparently needs a String

if __name__ == "__main__":
    app.run(port = 1337, debug=True) # Starts on Port 1337