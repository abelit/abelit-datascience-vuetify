from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

from flask_cors import CORS
import datetime

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


@app.route('/hello', methods=['GET'])
def index():
    return "hello world!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('name', None)
    password = request.json.get('password', None)
    # 在后台打印前端提交的数据
    print(username)
    print(password)
    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    access_expires = datetime.timedelta(seconds=60)
    refresh_expires = datetime.timedelta(seconds=120)
    ret = {
        'access_token': create_access_token(identity=username, expires_delta=access_expires),
        'refresh_token': create_refresh_token(identity=username, expires_delta=refresh_expires)
    }
    return jsonify(ret), 200


# The jwt_refresh_token_required decorator insures a valid refresh
# token is present in the request before calling this endpoint. We
# can use the get_jwt_identity() function to get the identity of
# the refresh token, and use the create_access_token() function again
# to make a new access token for this identity.
@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200


if __name__ == '__main__':
    app.run(debug=True)
