from flask import request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)
import datetime
from app.db import db
from app.models import User
from . import auth

from app import app

@auth.route('/')
def authpage():
    return "Auth page!"


@auth.route('/register', methods=['POST'])
def register():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    selected_department = request.json.get('selected_department', None)
    selected_position = request.json.get('selected_position', None)
    picked_gender = request.json.get('picked_gender', None)

    # 用户注册默认状态为0即不允许登录
    status = 0
    STATUSCODE = ''
    user = User(username=username, name=name, email=email, password=generate_password_hash(
    password), group_id=selected_department, position_id=selected_position, gender=picked_gender,status=status)

    # db.session.add(user)
    # db.session.commit()
    try:
        db.session.add(user)
        db.session.commit()
        STATUSCODE = 200
    except Exception as err:
        # print(err)
        app.logger.error(err)
        STATUSCODE = 500
        
    return jsonify(STATUSCODE)

@auth.route('/login', methods=['POST'])
def login():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # 获取用户信息
    user_by_name = User.query.filter_by(username=username).first()
    user_by_email = User.query.filter_by(email=username).first()

    # 组合使用用户名或邮箱进行登录
    user = user_by_name if user_by_name else user_by_email

    # 验证用户信息是否匹配
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    access_expires = datetime.timedelta(seconds=3600)
    refresh_expires = datetime.timedelta(seconds=86400)
    ret = {
        'access_token': create_access_token(identity=user.username, expires_delta=access_expires),
        'refresh_token': create_refresh_token(identity=user.username, expires_delta=refresh_expires)
    }
    return jsonify(ret), 200


# The jwt_refresh_token_required decorator insures a valid refresh
# token is present in the request before calling this endpoint. We
# can use the get_jwt_identity() function to get the identity of
# the refresh token, and use the create_access_token() function again
# to make a new access token for this identity.
@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_expires = datetime.timedelta(seconds=3600)
    ret = {
        'access_token': create_access_token(identity=current_user, expires_delta=access_expires)
    }
    return jsonify(ret), 200


@auth.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200