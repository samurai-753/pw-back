from flask import Flask, jsonify
from controller.ctrl_professor import CtrlProfessor

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello there'

@app.route('/professor/<idx>')
def get_professor(idx):
    idx = int(idx)
    return jsonify(CtrlProfessor().get_professor(idx).__dict__)

if __name__ == '__main__':
    app.run()