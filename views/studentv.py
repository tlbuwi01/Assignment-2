from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user, unset_jwt_cookies, set_access_cookies
from App.controllers.student_controller import StudentController
from App.controllers.accolade_controller import AccoladeController
from App.controllers.hours_controller import HoursController
from App.models.hours_recorded import HoursRecorded

#from App.controllers import ()

student_views = Blueprint('student_views', __name__, template_folder='../templates')


@student_views.route('/studentlogin', methods=['POST'])
def student_login_paage():
  data = request.json
  response,status = StudentController.login_student(data['username'],data['password'])
  if status != 200:
    return jsonify(message='bad username or password given'), status
  return response,200
  

@student_views.route('/student', methods=['POST'])
def create_user_action():
    data = request.json
    student, status = StudentController.create_student(data['name'],data['password'])
    if status == 201:
      return jsonify({'message ': f'Student created successfully with ID: {student.studentID}'}), status
    return jsonify(student), status
    


@student_views.route('/students/accolades', methods=['GET'])
#@jwt_required()
def get_student_accoldaes_page():
 data = request.json
 #student = StudentController.get_student_by_id(data['studentID'])#function to add
 accolades = AccoladeController.get_student_accolades(data['studentID'])
 return jsonify(f'{accolades}'),200


@student_views.route('/students/leaderboard', methods=['GET'])
def get_leaderboard_page():
   students = StudentController.get_leaderboard()#function to add
   return jsonify(message=f'{students}')


@student_views.route('/student/reqHours', methods=['POST'])
#@jwt_required()
def request_hours_page():
    data = request.json
    response,status  = HoursController.add_student_hours(data['studentID'],data['staffID'],data['amount'])
    return response,status

@student_views.route('/studentlogout', methods=['GET'])
def studentlogout():
  response = jsonify(message='Logged out')
  unset_jwt_cookies(response)
  return jsonify(message='Logged out')