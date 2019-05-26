from flask import Blueprint, jsonify, request
from controller import CtrlProfessor


app_professor = Blueprint('professor', __name__)
ctrl_professor = CtrlProfessor()


@app_professor.route('/api/professor/', methods=['GET'])
def get_professores():
    professores = ctrl_professor.get_professores()
    if professores == None:
        return jsonify(success=False)

    l = [ x.__dict__ for x in professores ]
    return jsonify(professores=l)


@app_professor.route('/api/professor/<idx>', methods=['GET'])
def get_professor(idx):
    idx = int(idx)
    p = ctrl_professor.get_professor(idx)
    if p == None:
        return jsonify(success=False)

    return jsonify(p.__dict__)


@app_professor.route('/api/professor', methods=['POST'])
def post_professor():
    data = request.get_json()
    try:
        r = ctrl_professor.add_professor(data)
    except KeyError as e:
        return jsonify(success=False, mensagem='Está faltando o dado {}'.format(e), code=400)
    
    return jsonify(idx=r)


@app_professor.route('/api/professor/<idx>', methods=['PUT'])
def update_professor(idx):
    idx = int(idx)
    data = request.get_json()
    r = ctrl_professor.update_professor(idx, data)
    
    return jsonify(success=r)


@app_professor.route('/api/professor/<idx>', methods=['DELETE'])
def delete_professor(idx):
    idx = int(idx)
    r = ctrl_professor.delete_professor(idx)
    return jsonify(success=r)