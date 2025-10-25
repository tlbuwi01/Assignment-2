from App.models.student import Student  
from App.database import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError # Good practice for robust error handling
from flask_jwt_extended import create_access_token,set_access_cookies
from flask import jsonify

class StudentController:

    @staticmethod
    def create_student(name,password):
        if not name or len(str(name).strip()) == 0:
            return {"error": "Student name cannot be empty."}, 400
        
        if not password or len(str(password).strip()) == 0:
            return {"error": "Student name cannot be empty."}, 400
        
        name = str(name).strip()

        if Student.query.filter_by(name=name).first():
             return {"error": f"Student with name '{name}' already exists."}, 409 # 409 Conflict

        try:
            student = Student(name=name,password=password)
            db.session.add(student)
            db.session.commit()
            return student, 201 
        
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            print(f"Database error during student creation: {e}") 
            return {"error": "An unexpected error occurred while saving the student."}, 500


    @staticmethod
    def get_all_students():
        """
        Retrieves all students.
        """
        students = Student.query.all()
        print(students)
        # Return list of model objects and 200 OK (even if list is empty)
        return students, 200 
    
    @staticmethod
    def get_leaderboard():
        students = Student.query.order_by(Student.totalHours.desc()).all()
        leaderboard = []
        rank = 1

        for student in students:
         leaderboard.append({
            "rank": rank,
            "id": student.studentID,
            "name": student.name,
            "totalHours": student.totalHours
            })
         rank += 1
        return leaderboard, 200


    @staticmethod
    def get_student_by_id(studentID):

    # 2. Database lookup
        student = Student.query.get(studentID)

    # 3. Determine response
        if student:
            return student, 200  # Found, return model object and 200 OK
        else:
            return {"error": f"Student with ID {studentID} not found."}, 404
        
    @staticmethod
    def login_student(name,password):
        student = Student.query.filter_by(name=name).first()
        if student and student.check_password(password) :
            token = create_access_token(identity=name)
            response = jsonify(access_token=token)
            set_access_cookies(response, token)
            return response,200
        return {"Invalid username or password"}, 401
