from App.models.student import Student  
from App.database import db

def create_student(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return student

def get_all_students():
    return Student.query.all()  

def get_student_by_id(studentID):
    return Student.query.get(studentID)  

