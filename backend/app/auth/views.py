from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)
import datetime
from sqlalchemy import or_,and_

from db import db
from models import User,Session

auth = Blueprint("auth", __name__)


def decorator_session(func):
    def wrapper(*args, **kw):
        print("session decorator")
        sess = Session(userid='1',ip=request.remote_addr,info=request.user_agent.platform+";"+request.user_agent.browser)
        try:
            db.session.add(sess)
            db.session.commit()
        except Exception:
            db.session.rollback()
            print("record session failed.")
        return func(*args,**kw)
    return wrapper

def create_session(userid,ip,status,info):
    sess = Session(userid=userid,ip=ip,status=status,info=info)
    try:
        db.session.add(sess)
        db.session.commit()
    except Exception:
        db.session.rollback()
        print("record session failed.")

@auth.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "module": "auth"
    })

@auth.route('/register', methods=['POST'])
def register():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    selected_department = request.json.get('selected_department', None)
    selected_position = request.json.get('selected_position', None)
    selected_gender = request.json.get('selected_gender', None)
    # 用户注册默认状态为0即不允许登录
    status = 0

    status_code = None

    user = User(username=username, name=name, email=email, password=generate_password_hash(
        password), group_id=selected_department, position_id=selected_position, gender=selected_gender, status=status)

    try:
        db.session.add(user)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@auth.route('/login', methods=['POST'])
def login():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    status_code = None
    result = None

    user_filter = {
        or_(User.name == username, User.email == username)
    }

    try:
        # 获取用户信息
        # user_by_name = User.query.filter_by(name=username).first()
        # user_by_email = User.query.filter_by(email=username).first()
        # # 组合使用用户名或邮箱进行登录
        # user = user_by_name if user_by_name else user_by_email
        print(request.user_agent)
        user = User.query.filter(*user_filter).first()
        # 验证用户信息是否匹配
        if not user or not check_password_hash(user.passwd, password):
            status_code = 401
        else:
            # Use create_access_token() and create_refresh_token() to create our
            # access and refresh tokens
            access_expires = datetime.timedelta(seconds=3600)
            refresh_expires = datetime.timedelta(seconds=86400)
            result = {
                'access_token': create_access_token(identity=user.name, expires_delta=access_expires),
                'refresh_token': create_refresh_token(identity=user.name, expires_delta=refresh_expires)
            }
            status_code = 200
    except:
        status_code = 500

    
    if status_code == 200:
        create_session(user.id,request.remote_addr,1, "user: " +str(request.remote_user) + ";" + "plateform: " + str(request.user_agent.platform) + ";" + "browser: " +str(request.user_agent.browser))

    return jsonify(result), status_code


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
    result = {
        'access_token': create_access_token(identity=current_user, expires_delta=access_expires)
    }
    return jsonify(result), 200


@auth.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200
