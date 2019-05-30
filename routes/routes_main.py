from flask import Blueprint, jsonify, request


app_main = Blueprint('main', __name__)


@app_main.route('/')
def home():
    return 'Hello there General Kenobi'
