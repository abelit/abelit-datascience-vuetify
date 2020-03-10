# coding:utf8
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import time


from db import db
from models import Groups, Positions, Users, Roles, Menus

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

    # 使用Groups模型类添加用户组
    group = Groups(name=name, enname=enname,
                  status=status, description=description)

    status_code = None

    try:
        db.session.add(group)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/group/delete', methods=['POST'])
def delete_group():
    # 从前端Ajax请求中获取用户名
    name = request.json.get('name', None)
    status_code = None

    group = Groups.query.filter_by(name=name).first()

    # 提交入库
    try:
        # 删除角色
        db.session.delete(group)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code

@admin.route('/group/update', methods=['POST'])
def update_group():
    # 从前端Ajax请求中获取角色信息
    name = request.json.get('name', None)
    status = request.json.get('status', None)
    description =  request.json.get('description', None)

    status_code = None

    group = Groups.query.filter_by(name=name)
    # 更新用户信息
    group.update({'status': status,'description': description})
            
    # 提交入库
    try:
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

    position = Positions(name=name, enname=enname,
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

@admin.route('/position/delete', methods=['POST'])
def delete_position():
    # 从前端Ajax请求中获取用户名
    name = request.json.get('name', None)
    status_code = None

    position = Positions.query.filter_by(name=name).first()

    # 提交入库
    try:
        # 删除角色
        db.session.delete(position)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code

@admin.route('/position/update', methods=['POST'])
def update_position():
    # 从前端Ajax请求中获取角色信息
    name = request.json.get('name', None)
    status = request.json.get('status', None)
    description =  request.json.get('description', None)

    status_code = None

    position = Positions.query.filter_by(name=name)
    # 更新用户信息
    position.update({'status': status,'description': description})
            
    # 提交入库
    try:
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route("/menu/add", methods=["POST"])
# @jwt_required
def add_menu():
    print("--------------------------------------------------+++++++++++++++++++++++++++++")
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

    print(".........................................")
    print(name)

    menu = Menus(name=name, en_name=enname, fid=fid, url=url, component=component, icon=icon,
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

    user = Users(username=username, name=name, email=email, password=generate_password_hash(
        password), group_id=selected_department, position_id=selected_position, gender=selected_gender, status=status)

    for r in role:
        user_role = Roles.query.get(r['id'])
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

    user_obj = Users.query.filter_by(username=username)
    user = user_obj.first()
    # 更新用户信息
    user_obj.update({'name': name, 'group_id': selected_department,
                 'position_id': selected_position, 'gender': selected_gender, 'status': status})

    # 根据用户输入判断是否进行密码更新
    if password is not None:
        user_obj.update({'password': generate_password_hash(password)})

    has_role = user.roles
    new_role = []

    # 更新用户权限信息
    for r in role:
        # 获取角色对象
        user_role = Roles.query.get(r['id'])
        new_role.append(user_role)

    # 删除没有的权限
    for hr in has_role:
        if hr not in new_role:
            user.roles.remove(hr)
    

    # 添加新增不存在的权限
    for nr in new_role:
        if nr not in has_role:
            user.roles.append(nr)
            
    # 提交入库
    try:
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/user/delete', methods=['POST'])
def delete_user():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    status_code = None
    print("...........................................")
    print(username)
    user = Users.query.filter_by(username=username).first()

    # 提交入库
    try:
        # 删除用户的权限
        for ur in user.roles:
            user.roles.remove(ur)
        db.session.commit()
        # 删除用户
        db.session.delete(user)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/user/list', methods=['GET'])
def list_users():
    result = []
    users = db.session.query(Users, Groups, Positions).join(Groups, Users.group_id == Groups.id).join(
        Positions, Users.position_id == Positions.id).all()

    for u in users:
        ulist = {
            "name": u.Users.name,
            "username": u.Users.username,
            "email": u.Users.email,
            "gender": u.Users.gender,
            "status": u.Users.status,
            "created_time": u.Users.created_time,
            "group": {"name": u.Groups.name, "id": u.Groups.id},
            "position": {"name": u.Positions.name, "id": u.Positions.id}
        }

        urole = []
        for r in u.Users.roles:
            urole.append({"name": r.name, "id": r.id})
        ulist["role"] = urole

        result.append(ulist)
    return jsonify(result), 200


@admin.route('/role/add', methods=['POST'])
def add_role():
    name = request.json.get('name', None)
    enname = request.json.get('enname', None)
    status = request.json.get('status', None)

    status_code = None

    role = Roles(name=name, enname=enname, status=status)

    try:
        db.session.add(role)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code

@admin.route('/role/update', methods=['POST'])
def update_role():
    # 从前端Ajax请求中获取角色信息
    name = request.json.get('name', None)
    status = request.json.get('status', None)

    status_code = None

    role = Roles.query.filter_by(name=name)
    # 更新用户信息
    role.update({'status': status})
            
    # 提交入库
    try:
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code

@admin.route('/role/delete', methods=['POST'])
def delete_role():
    # 从前端Ajax请求中获取用户名
    name = request.json.get('name', None)
    status_code = None

    role = Roles.query.filter_by(name=name).first()

    # 提交入库
    try:
        # 删除角色
        db.session.delete(role)
        db.session.commit()
        status_code = 200
    except Exception:
        status_code = 500

    return jsonify(), status_code


@admin.route('/role/list', methods=['GET'])
def list_roles():
    result = []
    roles = Roles.query.all()

    for r in roles:
        rlist = {
            "name": r.name,
            "enname": r.enname,
            "status": r.status,
            "created_time": r.created_time
        }
        result.append(rlist)
    return jsonify(result), 200
