from App.database import db  

student_accolade = db.Table('student_accolade', db.Column('studentID', db.Integer, 
                                                          db.ForeignKey('student.studentID')), 

db.Column('accoladeID', db.Integer, 
          
db.ForeignKey('accolade.accoladeID'))
)

class Accolade(db.Model):
    accoladeID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255))
    hoursNeeded = db.Column(db.Integer, nullable=False)  
