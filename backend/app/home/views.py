from flask import render_template, Blueprint,request,jsonify

home = Blueprint("home", __name__)


# 入口文件，通过入口文件跳转到vue前端
@home.route('/')
def index():
    # flash('You were successfully logged in')
    return render_template('index.html')

