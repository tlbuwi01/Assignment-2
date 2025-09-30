from App.database import db

class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    totalHours = db.Column(db.Integer, default=0)

    hours = db.relationship('HoursRecorded', backref='student', lazy=True)
    accolades = db.relationship('Accolade',
                                secondary='student_accolade', backref='students')