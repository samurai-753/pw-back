from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_optional, get_jwt_identity
from model import User


app_main = Blueprint('main', __name__)


@app_main.route('/')
def home():
    return 'Hello there General Kenobi'

@app_main.route('/api/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()
    if not user or password != user.password:
        return jsonify(
            status=401,
            message='Combinação de senha e email não encontrada'
        )

    access_token = create_access_token(identity=email)

    try:
        nome = user.professor.detalhes.nome
    except:
        nome = email

    return jsonify(
        access_token=access_token,
        nome=nome
    )

@app_main.route('/api/check', methods=['POST', 'GET'])
@jwt_optional
def check():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user), 200
    else:
        return jsonify(logged_in_as='anonymous user'), 200