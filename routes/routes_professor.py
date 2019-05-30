from flask import Blueprint, jsonify, request
from controller import CtrlProfessor, CtrlPessoa
from model import Professor, Pessoa
from pprint import pprint


app_professor = Blueprint('professor', __name__)
ctrl_professor = CtrlProfessor()
ctrl_pessoa = CtrlPessoa()


@app_professor.route('/api/professor/', methods=['GET'])
def get_professores():
    """
    @api {get} /api/professor Recupera professores
    @apiVersion 1.0.0-a
    @apiName GetProfessor
    @apiGroup Professor

    @apiDescription Recupera a lista de todos os professores castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>professor</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx": 1,
                    "nome": "Durelli",
                    "email": "durelli@dcc.ufla.br",
                    "telefone": "35912345678",
                    "sala": "DCC26",
                    "extensões": [
                        "Bacharel e ciência da computção, UFLA 2007"
                    ]
                }, {
                    ...
                }
            ]
        }
    """

    return jsonify(
        status=200,
        data={}
    )


@app_professor.route('/api/professor/<idx>', methods=['GET'])
def get_professor(idx):
    """
    @api {get} /api/professor/:id Recupera professor
    @apiVersion 1.0.0-a
    @apiName GetProfessorId
    @apiGroup Professor

    @apiDescription Recupera o professor com o <code>id</code> fornecido

    @apiUse ProfessorExemplo

    @apiUse ProfessorNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_professor.route('/api/professor', methods=['POST'])
def post_professor():
    """
    @api {post} /api/professor/:id Adiciona professor
    @apiVersion 1.0.0-a
    @apiName PostProfessor
    @apiGroup Professor

    @apiDescription Adiciona um novo professor

    @apiUse ObjetoPessoa
    @apiUse ObjetoProfessor

    @apiUse ProfessorExemplo
    """

    data = request.get_json()
    
    nome = data['nome']
    email = data['email']
    telefone = data.get('telefone')

    pessoa = Pessoa(nome, email, telefone)
    pessoa_dict = ctrl_pessoa.add_pessoa(pessoa)

    sala = data['sala']

    professor = Professor(pessoa_dict['idx'], sala)
    professor_dict = ctrl_professor.add_professor(professor)

    professor.detalhes = pessoa

    return jsonify(
        status=200,
        data=professor_dict
    )


@app_professor.route('/api/professor/<idx>', methods=['PUT'])
def update_professor(idx):
    """
    @api {put} /api/professor/:id Atualiza professor
    @apiVersion 1.0.0-a
    @apiName PutProfessor
    @apiGroup Professor

    @apiDescription Atualiza um professor existente

    @apiUse ObjetoPessoaMod
    @apiUse ObjetoProfessorMod

    @apiUse ProfessorNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_professor.route('/api/professor/<idx>', methods=['DELETE'])
def delete_professor(idx):
    """
    @api {delete} /api/professor/:id Deleta professor
    @apiVersion 1.0.0-a
    @apiName DeleteProfessor
    @apiGroup Professor

    @apiDescription Deleta um professor existente

    @apiUse ObjetoPessoaMod
    @apiUse ObjetoProfessorMod

    @apiUse ProfessorNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )