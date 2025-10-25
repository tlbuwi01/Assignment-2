from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user, unset_jwt_cookies, set_access_cookies
from App.models.hours_recorded import HoursRecorded    

from App.controllers import (
  get_all_students,
  login_student,
  get_student_by_id,
  add_student_hours,
  create_student
)

hours_views = Blueprint('hours_views', __name__, template_folder='../templates')