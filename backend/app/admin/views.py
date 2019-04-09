# coding:utf8
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash


from db import db
from models import Group, Position, User

admin = Blueprint("admin", __name__)
 
@admin.route("/")
def index():
	return "<h1> Admin Page</h1>"


@admin.route("/group/add", methods=["POST"])
# @jwt_required
def addGroup():
	 # 从前端Ajax请求中获取数据
    name = request.json.get('name', None)
    enname = request.json.get('enname', None)
    status = request.json.get('status', None)
    description = request.json.get('description', None)

    print(description)

    group = Group(name=name, enname=enname,status=status, description=description)

    try:
        db.session.add(group)
        db.session.commit()
        STATUSCODE = 200
    except Exception as err:
        print(err)
        STATUSCODE = 500

    return jsonify(STATUSCODE)


@admin.route("/position/add", methods=["POST"])
# @jwt_required
def addPosition():
	 # 从前端Ajax请求中获取数据
    name = request.json.get('name', None)
    enname = request.json.get('enname', None)
    status = request.json.get('status', None)
    description = request.json.get('description', None)

    position = Position(name=name, enname=enname,
                  status=status, description=description)

    try:
        db.session.add(position)
        db.session.commit()
        STATUSCODE = 200
    except Exception as err:
        print(err)
        STATUSCODE = 500

    return jsonify(STATUSCODE)


@admin.route('/user/add', methods=['POST'])
def addUser():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    selected_department = request.json.get('selected_department', None)
    selected_position = request.json.get('selected_position', None)
    picked_gender = request.json.get('picked_gender', None)
    status = request.json.get('status', None)

    print(picked_gender)

    STATUSCODE = ''
    user = User(username=username, name=name, email=email, password=generate_password_hash(
        password), group_id=selected_department, position_id=selected_position, gender=picked_gender, status=status)

    try:
          # 检测用户是否已经存在
        isExistUser = User.query.filter_by(username=username).first()
        # isExistEmail = User.query.filter_by(email=email).first()

        if isExistUser:
            return jsonify(600)

        db.session.add(user)
        db.session.commit()
        STATUSCODE = 200
    except Exception as err:
        print(err)
        STATUSCODE = 500

    return jsonify(STATUSCODE)
