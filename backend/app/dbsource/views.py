# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/03/21 08:31:55
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask import jsonify, request, Blueprint, g
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Group, Position, User, Role, Menu
from db import db

dbsource = Blueprint("dbsource", __name__)


@dbsource.route('/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__
    })


@dbsource.route('/group', methods=['GET'])
def group():
    result = []
    status_code = None
    try:
        group = Group.query.all()
        status_code = 200
        for g in group:
            result.append({
                "id": g.id,
                "name": g.name,
                "enname": g.enname,
                "status": g.status,
                "description": g.description,
                "created_time": g.created_time
            })
    except Exception:
        status_code = 500

    return jsonify(result), status_code


@dbsource.route('/position', methods=['GET'])
def position():
    result = []
    position = Position.query.all()

    for p in position:
        result.append({
            "id": p.id,
            "name": p.name,
            "enname": p.enname,
            "status": p.status,
            "description": p.description,
            "created_time": p.created_time
        })

    return jsonify(result), 200


@dbsource.route('/role', methods=['GET'])
def role():
    result = []
    role = Role.query.filter_by(status=1)

    for r in role:
        result.append({
            "id": r.id,
            "name": r.name,
        })

    return jsonify(result), 200


@dbsource.route('/menu', methods=['GET'])
# @jwt_required
def menu():
    menus = Menu.query.all()
    result = []

    for m in menus:
        result.append({
            "id": m.id,
            "name": m.name,
            "enname": m.en_name,
            "fid": m.fid,
            "url": m.url,
            "component": m.component,
            "icon": m.icon,
            "status": m.status,
            "type": m.type,
            "order": m.order,
            "created_time": m.created_time
        })

    return jsonify(result), 200


@dbsource.route('/test/menu')
def test_menu():
    sqlres = db.engine.execute(
        """select id,name,alias,surname,email from users""")
    result = []

    for i in sqlres:
        result.append({"id": i.id, "name": i.name, "alias": i.alias,
                       "surname": i.surname, "email": i.email})

    return jsonify(result)


@dbsource.route('/checkusername', methods=['GET'])
def check_username():
    # 从前端Ajax请求中获取用户名
    username = request.args.get('username')

    status_code = None

    try:
        user = User.query.filter_by(username=username).first()
        status_code = 200
        if user:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code


@dbsource.route('/checkemail', methods=['GET'])
def check_email():
    # 从前端Ajax请求中获取用户名
    email = request.args.get('email')

    status_code = None

    try:
        email = User.query.filter_by(email=email).first()
        status_code = 200
        if email:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code


@dbsource.route('/checkgroup', methods=['GET'])
def check_group():
    # 从前端Ajax请求中获取用户名
    name = request.args.get('name')

    status_code = None

    try:
        group = Group.query.filter_by(name=name).first()
        status_code = 200
        if group:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code


@dbsource.route('/checkposition', methods=['GET'])
def check_position():
    # 从前端Ajax请求中获取用户名
    name = request.args.get('name')

    status_code = None

    try:
        position = Position.query.filter_by(name=name).first()
        status_code = 200
        if position:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code
