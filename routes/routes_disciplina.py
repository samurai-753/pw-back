from flask import Blueprint, jsonify


app_disciplina = Blueprint('disciplina', __name__)


@app_disciplina.route('/api/disciplina', methods=['GET'])
def get_disciplina():
    """
    @api {get} /api/disciplina Recupera disciplinas
    @apiVersion 1.0.0-a
    @apiName GetDisciplinas
    @apiGroup Disciplina

    @apiDescription Recupera a lista de todos os disciplinas castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>Disciplina</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx": 485,
                    "tipo_disciplia": "Graduação",
                    "idx_professor": 2563,
                    "idx_documento": [ 45663, 45226 ]
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


@app_disciplina.route('/api/disciplina/<idx>', methods=['GET'])
def get_disciplina_idx(idx):
    """
    @api {get} /api/disciplina/:id Recupera disciplina
    @apiVersion 1.0.0-a
    @apiName GetDisciplinaId
    @apiGroup Disciplina

    @apiDescription Recupera o aluno com o <code>id</code> fornecido

    @apiUse DisciplinaExemplo

    @apiUse DisciplinaNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_disciplina.route('/api/disciplina', methods=['POST'])
def post_disciplina():
    """
    @api {post} /api/disciplina/ Adiciona disciplina
    @apiVersion 1.0.0-a
    @apiName PostDisciplina
    @apiGroup Disciplina

    @apiDescription Adiciona um novo <code>Disciplina</code>

    @apiUse ObjetoDisciplina

    @apiUse DisciplinaExemplo
    """

    return jsonify(
        status=200,
        data={}
    )


@app_disciplina.route('/api/disciplina/<idx>', methods=['PATCH'])
def update_disciplina(idx):
    """
    @api {patch} /api/disciplina/:id Atualiza disciplina
    @apiVersion 1.0.0-a
    @apiName PutDisciplina
    @apiGroup Disciplina

    @apiDescription Atualiza um <code>Disciplina</code> existente

    @apiUse ObjetoDisciplinaMod

    @apiUse DisciplinaNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_disciplina.route('/api/disciplina/<idx>', methods=['DELETE'])
def delete_disciplina(idx):
    """
    @api {delete} /api/disciplina/:id Deleta disciplina
    @apiVersion 1.0.0-a
    @apiName DeleteDisciplina
    @apiGroup Disciplina

    @apiDescription Deleta um <code>Disciplina</code> existente

    @apiUse DisciplinaNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )