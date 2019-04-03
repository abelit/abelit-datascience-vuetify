# coding:utf8
 
from . import admin 
 
@admin.route("/")
def index():
	return "<h1> Admin Page</h1>"