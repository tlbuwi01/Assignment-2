from App.database import db

class Staff(db.Model):
    staffID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    confirmedHours = db.relationship('HoursRecorded', backref='staff', lazy=True)