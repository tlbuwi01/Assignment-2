import fask
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from App.controllers import (
    create_staff,
    login_staff,
    unset_jwt_cookies,
    jwt_required,
    confirm_hours,
    confirm_student_hours,
    create_accolade,
    award_accolade
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')

@staff_views.route('/newstaff/<name>/<password>', methods=['GET'])
def create_staff_action(name, password):
    create_staff(name, password)
    return jsonify({"message":"Staff Created"})  


@staff_views.route('/login', methods=['POST'])
def staff_login_page(staffID,password):
  data = request.json
  response = login_staff(data['username'], data['password'])
  if not response:
    return jsonify(message='bad username or password given'), 403
  return response

@staff_views.route('/<staff>/confirm_hours', methods=['POST'])
@jwt_required
def confirm_hours_page(recordID,staffID):
  response= confirm_hours(recordID,staffID)
  return response

@staff_views.route('/<staff>/change_hours', methods=['POST'])
@jwt_required
def confirm_hours_page(hour_id):
  response= confirm_student_hours(hour_id)
  return response


@staff_views.route('/stafflogout', methods=['GET'])
@jwt_required
def logout():
  response = jsonify(message='Logged out')
  unset_jwt_cookies(response)
  return response

@staff_views.route('/<staff>/create_accolade', methods=['POST'])
@jwt_required
def create_accolade_page(name, description):
  response= create_accolade(name, description)
  return response

@staff_views.route('/<staff>/award_accolade', methods=['POST'])
@jwt_required
def create_accolade_page(student_id, accolade_id):
  response= award_accolade(student_id, accolade_id)
  return response