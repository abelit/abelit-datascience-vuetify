from flask import jsonify, request, Blueprint,g
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Groups, Positions, Users, Roles, Menus
from db import db

api = Blueprint("api", __name__)


@api.route('/group', methods=['GET'])
def group():
    result = []
    status_code = None
    try:
        group = Groups.query.all()
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


@api.route('/position', methods=['GET'])
def position():
    result = []
    position = Positions.query.all()

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


@api.route('/role', methods=['GET'])
def role():
    result = []
    role = Roles.query.filter_by(status=1)

    for r in role:
        result.append({
            "id": r.id,
            "name": r.name,
        })

    return jsonify(result), 200


@api.route('/menu', methods=['GET'])
# @jwt_required
def menu():
    menus = Menus.query.all()
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


@api.route('/ping')
def ping():
    return 'Pong!'

@api.route('/test/menu')
def test_menu():
    sqlres = db.engine.execute("""select id,name,alias,surname,email from users""")
    result = []

    for i in sqlres:
        result.append({"id": i.id, "name": i.name, "alias": i.alias,
                       "surname": i.surname, "email": i.email})

    return jsonify(result)


@api.route('/checkusername', methods=['GET'])
def check_username():
    # 从前端Ajax请求中获取用户名
    username = request.args.get('username')

    status_code = None

    try:
        user = Users.query.filter_by(username=username).first()
        status_code = 200
        if user:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code


@api.route('/checkemail', methods=['GET'])
def check_email():
    # 从前端Ajax请求中获取用户名
    email = request.args.get('email')

    status_code = None

    try:
        email = Users.query.filter_by(email=email).first()
        status_code = 200
        if email:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code


@api.route('/checkgroup', methods=['GET'])
def check_group():
    # 从前端Ajax请求中获取用户名
    name = request.args.get('name')

    status_code = None

    try:
        group = Groups.query.filter_by(name=name).first()
        status_code = 200
        if group:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code


@api.route('/checkposition', methods=['GET'])
def check_position():
    # 从前端Ajax请求中获取用户名
    name = request.args.get('name')

    status_code = None

    try:
        position = Positions.query.filter_by(name=name).first()
        status_code = 200
        if position:
            status_code = 700
    except:
        status_code = 500

    return jsonify(), status_code
