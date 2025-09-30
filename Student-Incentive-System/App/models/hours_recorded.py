from App.database import db

class HoursRecorded(db.Model):
    recordId = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    confirmed = db.Column(db.Boolean, default=False)
    
    # Foreign key to Student
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    
    # Foreign key to Staff
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)  