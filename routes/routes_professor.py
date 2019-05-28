from flask import Blueprint, jsonify, request
from controller import CtrlProfessor


app_professor = Blueprint('professor', __name__)
ctrl_professor = CtrlProfessor()


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

    professores = ctrl_professor.get_professores()
    if professores == None:
        return jsonify(success=False)

    l = [ x.__dict__ for x in professores ]
    return jsonify(professores=l)


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

    idx = int(idx)
    p = ctrl_professor.get_professor(idx)
    if p == None:
        return jsonify(success=False)

    return jsonify(p.__dict__)


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
    try:
        r = ctrl_professor.add_professor(data)
    except KeyError as e:
        return jsonify(success=False, mensagem='Está faltando o dado {}'.format(e), code=400)
    
    return jsonify(idx=r)


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

    idx = int(idx)
    data = request.get_json()
    r = ctrl_professor.update_professor(idx, data)
    
    return jsonify(success=r)


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

    idx = int(idx)
    r = ctrl_professor.delete_professor(idx)
    return jsonify(success=r)