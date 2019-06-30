import json
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init the app
app = Flask(__name__)

# Config the data base
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', 'sqlite://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)


if __name__ == '__main__':
    port = os.getenv('PORT', 58913)

    from routes import *
    app.register_blueprint(app_main)
    app.register_blueprint(app_professor)
    app.register_blueprint(app_aluno)

    app.run(host='0.0.0.0', port=port, debug=True)