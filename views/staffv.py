
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from App.controllers.staff_controller import StaffController
from App.controllers.accolade_controller import AccoladeController
from App.controllers import (
    unset_jwt_cookies   
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')

@staff_views.route('/newstaff', methods=['POST'])
def create_staff_action():
  data = request.json
  staff,status= StaffController.createstaff(data['name'],data['password'])
  if status == 201:
    return jsonify({'message ': f'Staff created successfully with ID: {staff.staffID}'}), status
  return jsonify(staff), status

@staff_views.route('/stafflogin', methods=['POST'])
def staff_login_page():
  data = request.json
  response = StaffController.login_staff(data['name'], data['password'])
  if not response:
    return jsonify(message='bad username or password given'), 403
  return response

@staff_views.route('/staff/confirm_hours', methods=['PUT'])
#@jwt_required()
def confirm_hours_page():
    data = request.json
    response = StaffController.confirm_hours(data['recordID'], data["staffID"])
    return response

@staff_views.route('/staff/accolade' , methods=['POST'])
#@jwt_required()
def create_accolade_page():
    data = request.json
    response, status = AccoladeController.create_accolade(data['name'], data['description'],data['hours_needed'])
    if status != 201:
      return response, status
    else:
       return jsonify(f'{response}'), status

@staff_views.route('/awardaccolade', methods=['POST'])
#@jwt_required()
def award_accolade_page():
    data = request.json
    response, status = AccoladeController.award_accolade(data['student_id'], data['accolade_id'])
    return jsonify(f'{response}'), status


@staff_views.route('/stafflogout', methods=['GET'])
def stafflogout():
  response = jsonify(message='Logged out')
  unset_jwt_cookies(response)
  return response

