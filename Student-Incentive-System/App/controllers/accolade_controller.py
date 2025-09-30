from App.models.accolade import Accolade  
from App.models.student import Student
from App.database import db

def award_accolade(studentID, accoladeID):
    student = Student.query.get(studentID)
    accolade = Accolade.query.get(accoladeID)
    if student and accolade:
        student.accolades.append(accolade)
        db.session.commit()
        return True
        return False  


