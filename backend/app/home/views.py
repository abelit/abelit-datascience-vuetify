from flask import render_template
from flask import Blueprint

home = Blueprint("home", __name__)


# 入口文件，通过入口文件跳转到vue前端
@home.route('/')
def index():
    return render_template('index.html')

@home.route('/hello')
def hello():
    return "hello world"
