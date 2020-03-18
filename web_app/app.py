from datetime import datetime
import sys
sys.path.append('./../database')
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from database import *
from flask_bootstrap import Bootstrap
import re

app = Flask(__name__)

Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lbbpsniacrpnhr:6fe2147cb3740ab3286f1ab803576a2bfb796283c947208c8bb3a2d9adc29b86@ec2-35-175-170-131.compute-1.amazonaws.com:5432/dc304919nvvflp'
db = SQLAlchemy(app)


@app.route("/")
def index():
    obj = UpdateDB()
    temp = obj.classRooms()
    return render_template("index.html", rooms=temp)

@app.route("/search")
def search():
    search_term = "^" + request.args.get('query')
    rooms = Rooms.query.all()
    output = []
    for room in rooms:

        if(re.search(search_term, room.room_number)):
            output.append(room)
    

    return render_template("index.html", rooms=output)

@app.route("/map")
def map():

    return render_template("map.html")


@app.route("/top5")
def topFive():

    rooms = Rooms.query.all()
    rooms_crowd = []
    output = []
    for room in rooms:
        rooms_crowd.append((room, room.number_of_students/room.room_capacity))

    rooms_crowd.sort(key=lambda x:x[1])

    for i in range(5):
        output.append(rooms_crowd[i][0])
    

    return render_template("index.html", rooms = output)

   

@app.route("/worst5")
def worstFive():
    rooms = Rooms.query.all()
    rooms_crowd = []
    output = []
    for room in rooms:
        rooms_crowd.append((room, room.number_of_students/room.room_capacity))

    rooms_crowd.sort(key=lambda x:x[1])

    for i in range(5):
        output.append(rooms_crowd[len(rooms_crowd)-1 -i][0])
    

    return render_template("index.html", rooms = output)
  

@app.route("/trends")
def trends():
    return render_template("trends.html")


@app.route("/monday")
def monday():
    return render_template("monday.html")
if __name__ == '__main__':
    app.run(debug=True)

