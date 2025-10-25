from App.database import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

# Helper for the many-to-many relationship
student_accolade = db.Table('student_accolade',
    db.Column('studentID', db.Integer, db.ForeignKey('student.studentID'), primary_key=True),
    db.Column('accoladeID', db.Integer, db.ForeignKey('accolade.accoladeID'), primary_key=True)
)


class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    totalHours = db.Column(db.Integer, default=0)

    hours = db.relationship('HoursRecorded', backref='student', lazy=True)
    accolades = db.relationship('Accolade',
                                secondary=student_accolade, 
                                backref=db.backref('students', lazy='dynamic'),
                                lazy='dynamic')
    password = db.Column(db.String(128), nullable=True) 
    
    def __init__(self, name,password):
        self.name = name 
        self.set_password(password)

    def __repr__(self):
        return f'<Student {self.studentID}: {self.name}: {self.totalHours} totalhours>'

    def to_dict(self):
        """Converts the model object into a dictionary for API response."""
        accolade_list = []
        # Safely serialize accolades if loaded
        if self.accolades:
            accolade_list = [accolade.to_dict() for accolade in self.accolades.all()]

        return {
            'studentID': self.studentID,
            'name': self.name,
            'totalHours': self.totalHours,
            'accolades': accolade_list,
        }
    def get_totalHours(self):
        return self.totalHours
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


