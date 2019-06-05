# coding:utf8
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import time


from db import db
from models import Group, Position, User, Role, Menu

admin = Blueprint("admin", __name__)


@admin.route("/")
def index():
    return "<h1> Admin Page</h1>"


@admin.route("/group/add", methods=["POST"])
# @jwt_required
def add_group():
         # 从前端Ajax请求中获取数据
    name = request.json.get('name', None)
    enname = request.json.get('enname', None)
    status = request.json.get('status', None)
    description = request.json.get('description', None)

    # 使用Group模型类添加用户组
    group = Group(name=name, enname=enname,
                  status=status, description=description)

    status_code = None

    try:
        db.session.add(group)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route("/position/add", methods=["POST"])
# @jwt_required
def add_position():
         # 从前端Ajax请求中获取数据
    name = request.json.get('name', None)
    enname = request.json.get('enname', None)
    status = request.json.get('status', None)
    description = request.json.get('description', None)

    position = Position(name=name, enname=enname,
                        status=status, description=description)

    status_code = None

    try:
        db.session.add(position)
        db.session.commit()
        status_code = 200
    except Exception as err:
        print(err)
        status_code = 500

    return jsonify(), status_code


@admin.route("/menu/add", methods=["POST"])
# @jwt_required
def add_menu():
    # 从前端Ajax请求中获取数据
    name = request.json.get('name', None)
    enname = request.json.get('enname', None)
    fid = request.json.get('fid', None)
    url = request.json.get('url', None)
    icon = request.json.get('icon', None)
    component = request.json.get('component', None)
    status = request.json.get('status', None)
    type = request.json.get('type', None)
    order = request.json.get('order', None)    

    menu = Menu(name=name, en_name=enname, fid=fid,url=url,component=component,icon=icon,
                        status=status, type=type, order=order)

    status_code = None

    try:
        db.session.add(menu)
        db.session.commit()
        status_code = 200
    except Exception as err:
        print(err)
        status_code = 500

    return jsonify(), status_code


@admin.route('/user/add', methods=['POST'])
def add_user():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    selected_department = request.json.get('selected_department', None)
    selected_position = request.json.get('selected_position', None)
    selected_gender = request.json.get('selected_gender', None)
    status = request.json.get('status', None)
    role = request.json.get('role', None)

    status_code = None

    user = User(username=username, name=name, email=email, password=generate_password_hash(
        password), group_id=selected_department, position_id=selected_position, gender=selected_gender, status=status)

    for r in role:
        user_role = Role.query.get(r['id'])
        user.roles.append(user_role)

    try:
        db.session.add(user)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/user/update', methods=['POST'])
def update_user():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    selected_department = request.json.get('selected_department', None)
    selected_position = request.json.get('selected_position', None)
    selected_gender = request.json.get('selected_gender', None)
    status = request.json.get('status', None)
    role = request.json.get('role', None)

    status_code = None

    user = User.query.filter_by(username=username)
    print("test ............")
    # 更新用户信息
    user.update({'name': name,'password': password, 'selected_department': selected_department, 'selected_position': selected_position,'selected_gender': selected_gender, 'status': status})

    has_role  = user.first().roles
    new_role = []

  
    # 更新用户权限信息
    for r in role:
        # 获取角色对象
        user_role = Role.query.get(r['id'])
        new_role.append(user_role)

    # 删除没有的权限
    for hr in has_role:
        if hr not in new_role:
            user.first().roles.remove(hr)

     # 添加新增不存在的权限
    for nr in new_role:
        if nr not in has_role:
            user.first().roles.append(nr)

    try:
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/user/list', methods=['GET'])
def list_users():
    result = []
    users = db.session.query(User,Group,Position).join(Group, User.group_id == Group.id).join(
        Position, User.position_id == Position.id).all()

    for u in users:
        ulist = {
            "name": u.User.name,
            "username": u.User.username,
            "email": u.User.email,
            "gender": u.User.gender,
            "status": u.User.status,
            "created_time": u.User.created_time,
            "group": {"name": u.Group.name, "id": u.Group.id},
            "position": {"name": u.Position.name, "id": u.Position.id}
        }
        # urole = []
        # for r in u.User.roles:
        #     urole.append(r.name)
        
        # ulist["role"] = ','.join(urole)

        urole = []
        for r in u.User.roles:
            urole.append({"name": r.name, "id": r.id})
        ulist["role"] = urole

        result.append(ulist)
    return jsonify(result), 200

@admin.route('/role/add', methods=['POST'])
def add_role():
    name = request.json.get('name', None)
    status = request.json.get('status', None)

    status_code = None

    role = Role(name=name, status=status)

    try:
        db.session.add(role)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/role/list', methods=['GET'])
def list_roles():
    result = []
    roles = Role.query.all()

    for r in roles:
        rlist = {
            "name": r.name,
            "status": r.status,
            "created_time": r.created_time
        }
        result.append(rlist)
    return jsonify(result), 200
