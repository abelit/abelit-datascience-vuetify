# coding:utf8
from flask import Blueprint

admin = Blueprint("admin", __name__)
 
@admin.route("/")
def index():
	return "<h1> Admin Page</h1>"
