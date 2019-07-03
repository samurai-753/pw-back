from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_optional, get_jwt_identity
from model import User


app_main = Blueprint('main', __name__)


@app_main.route('/')
def home():
    return 'Hello there General Kenobi'

@app_main.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"msg": "Email not found"}), 400
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

@app_main.route('/check', methods=['POST', 'GET'])
@jwt_optional
def check():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user), 200
    else:
        return jsonify(logged_in_as='anonymous user'), 200