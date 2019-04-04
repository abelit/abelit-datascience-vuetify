# coding:utf8
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint

from db import db

admin = Blueprint("admin", __name__)
 
@admin.route("/")
def index():
	return "<h1> Admin Page</h1>"


@admin.route("/addgroup", methods=["POST"])
@jwt_required
def addGroup():
	 # 从前端Ajax请求中获取数据
    name = request.json.get('name', None)
    status = request.json.get('status', None)

    group = Group(name=name, status=status)

    try:
        db.session.add(group)
        db.session.commit()
        STATUSCODE = 200
    except Exception as err:
        print(err)
        STATUSCODE = 500

    return jsonify(STATUSCODE)
