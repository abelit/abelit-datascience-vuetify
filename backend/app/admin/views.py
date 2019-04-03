# coding:utf8
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint

from db import db

admin = Blueprint("admin", __name__)
 
@admin.route("/")
def index():
	return "<h1> Admin Page</h1>"



