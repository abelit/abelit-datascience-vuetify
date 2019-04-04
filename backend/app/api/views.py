from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Group, Position,User


api = Blueprint("api", __name__)


@api.route('/group', methods=['GET'])
def group():
    result = []
    group = Group.query.all()
    
    for g in group:
        result.append({
            "id": g.id,
            "name": g.name
        })

    return jsonify(result)


@api.route('/position', methods=['GET'])
def position():
    result = []
    position = Position.query.filter_by(status=1)

    for p in position:
        result.append({
            "id": p.id,
            "name": p.name,
        })

    return jsonify(result)


@api.route('/menu', methods=['GET'])
@jwt_required
def menu():
    username = get_jwt_identity()
    if username == 'test':
        return jsonify({'mapdemo': '/demo/mapdemo', 'uidemo': '/demo/uidemo'})

    return jsonify({'uidemo': '/demo/uidemo'})


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


@api.route('/checkuser', methods=['GET'])
def checkUser():
    # 从前端Ajax请求中获取用户名
    username = request.args.get('username')
    email = request.args.get('email')
    existUsername = False
    existEmail = False
    result = {}

    try:
        user=User.query.filter_by(username=username).first()
        mail=User.query.filter_by(email=email).first()

        if user:
            existUsername = True
        if mail:
            existEmail = True

        result = {
            "status": 200,
            "existUsername": existUsername,
            "existEmail": existEmail
        }
    except:
        result = {
            "status": 500,
            "existUsername": existUsername,
            "existEmail": existEmail
        }

    return jsonify(result)
