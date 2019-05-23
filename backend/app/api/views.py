from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Group, Position, User, Tmenu, Role, Menu
from db import db

api = Blueprint("api", __name__)


@api.route('/group', methods=['GET'])
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


@api.route('/position', methods=['GET'])
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


@api.route('/role', methods=['GET'])
def role():
    result = []
    role = Role.query.filter_by(status=1)

    for r in role:
        result.append({
            "id": r.id,
            "name": r.name,
        })

    return jsonify(result), 200


@api.route('/menu', methods=['GET'])
# @jwt_required
def menu():
    # username = get_jwt_identity()
    # if username == 'test':
    #     return jsonify({'mapdemo': '/demo/mapdemo', 'uidemo': '/demo/uidemo'})

    # return jsonify({'uidemo': '/demo/uidemo'})
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


@api.route('/books', methods=['GET'])
def all_books():
    BOOKS = [
        {
            'title': 'On the Road',
            'author': 'Jack Kerouac',
            'read': True
        },
        {
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'author': 'J. K. Rowling',
            'read': False
        },
        {
            'title': 'Green Eggs and Ham',
            'author': 'Dr. Seuss',
            'read': True
        },
        {
            'title': 'Data Science',
            'author': 'Abelit',
            'read': True
        }
    ]
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


@api.route('/ping')
def ping():
    return 'Pong!'


@api.route('/tmenu')
def tmenu():
    tm = Tmenu.query.all()
    result = []

    for i in tm:
        result.append({"id": i.id, "name": i.name, "fid": i.fid})

    return jsonify(result)


@api.route('/mmenu')
def mmenu():
    tm = db.engine.execute("""with RECURSIVE t(id, name, fid, depth, path, cycle) as
                           (
        select a.id, a.name, a.fid, 1, array[a.id], false from tmenu a where id=1
        union all
        select b.id, b.name, b.fid, c.depth+1, path ||b.id, b.id=any(path) from tmenu b, t c where c.id=b.fid and not cycle
    )
        select * from t
        """)
    result = []

    for i in tm:
        result.append({"id": i.id, "name": i.name, "fid": i.fid,
                       "depth": i.depth, "path": i.path, "cycle": i.cycle})

    return jsonify(result)


@api.route('/checkusername', methods=['GET'])
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


@api.route('/checkemail', methods=['GET'])
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


@api.route('/checkgroup', methods=['GET'])
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


@api.route('/checkposition', methods=['GET'])
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
