from datetime import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://lbbpsniacrpnhr:6fe2147cb3740ab3286f1ab803576a2bfb796283c947208c8bb3a2d9adc29b86@ec2-35-175-170-131.compute-1.amazonaws.com:5432/dc304919nvvflp"



db = SQLAlchemy(app)


# @app.route("/")
# def index():
#     return render_template("index.html")

# create a table 
class Rooms(db.Model):
    __tablename__ = "Rooms"
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False)
    room_capacity = db.Column(db.Integer, nullable=False)
    number_of_students = db.Column(db.Integer)
    temperature_in_celsuis = db.Column(db.Integer)
    humidity_in_percent = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.now)

class MondayTrend(db.Model):
    __tablename__ = "MondayTrend"
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False)
    room_capacity = db.Column(db.Integer, nullable=False)
    number_of_students = db.Column(db.Integer)
    temperature_in_celsuis = db.Column(db.Integer)
    humidity_in_percent = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.now)

class TuesdayTrend(db.Model):
    __tablename__ = "TuesdayTrend"
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False)
    room_capacity = db.Column(db.Integer, nullable=False)
    number_of_students = db.Column(db.Integer)
    temperature_in_celsuis = db.Column(db.Integer)
    humidity_in_percent = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.now)



class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String, nullable=False)

class UpdateDB():

    # create an exception when user try to create the same room number
    def createRoom(self, room_number, room_capacity, number_of_students, temperature_in_celsuis, humidity_in_percent):
        room = Rooms(room_number=room_number, 
                    room_capacity=room_capacity,
                    number_of_students = number_of_students,
                    temperature_in_celsuis = temperature_in_celsuis,
                    humidity_in_percent =humidity_in_percent)
        db.session.add(room)
        db.session.commit()
        return False



    # function that increment number students in a particular room
    def incrementNumberStudent(self, room_number):
        room = Rooms.query.filter_by(room_number = room_number).first()   
        room.number_of_students +=1 
        db.session.commit()
        return False

    # function that decrement number students in particular room 
    def decrementNumberStudent(self, room_number):
        room = Rooms.query.filter_by(room_number = room_number).first()
        room.number_of_students -=1 
        db.session.commit()
        return False


    # function that query the number students in a particular room 
    def numberStudent(self, room_number):
        numberStudent = Rooms.query.filter_by(room_number = room_number).first().number_of_students
        return numberStudent

    def updateTemperature(self, room_number, temp_c):
        room = Rooms.query.filter_by(room_number=room_number).first()
        room.temperature_in_celsuis = temp_c
        db.session.commit()
        return False

    def updateHum(self, room_number, hum):
        room = Rooms.query.filter_by(room_number=room_number).first()
        room.humidity_in_percent = hum
        db.session.commit()
        return False
    # return a dictionary that have key(room number) and value(number of students in the room)
    def classRooms(self):
        rooms = Rooms.query.all()
        
        return rooms

def main():


    # create a class to create room row 
    obj = UpdateDB()

    obj.createRoom("14-001", 40, 10, 25, 30)
    

    # test increment and decrement students in room 14-001
    while (True):
        for i in range(50):
            obj.updateTemperature("14-001", i)
            obj.updateHum("14-001", i)
            obj.incrementNumberStudent("14-001")
            if(i % 2):
                obj.decrementNumberStudent("14-001")
            sleep(1)

        for i in range(10):
            obj.decrementNumberStudent("14-001")
            sleep(1)




 


if __name__ == '__main__':
    main()

