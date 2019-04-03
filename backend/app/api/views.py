from flask import jsonify
from . import api
from app.models import Group,Position


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
