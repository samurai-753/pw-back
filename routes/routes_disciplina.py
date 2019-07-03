from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controller import CtrlDisciplina
from exception import ExceptionDisciplinaNaoEncontrado, ExceptionDisciplinaCampoInvalido


app_disciplina = Blueprint('disciplina', __name__)
ctrl_disciplina = CtrlDisciplina()


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
        data=ctrl_disciplina.get_disciplinas()
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

    try:
        dis = ctrl_disciplina.get_disciplina(idx)
        return jsonify(
            status=200,
            data=dis
        )
    except ExceptionDisciplinaNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )


@app_disciplina.route('/api/disciplina', methods=['POST'])
@jwt_required
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

    try:
        data = request.get_json()
        dis = ctrl_disciplina.add_disciplina(data)
        return jsonify(
            status=200,
            data=dis
        )
    except ExceptionDisciplinaCampoInvalido as e:
        return jsonify(
            status=400,
            message=str(e)
        )


@app_disciplina.route('/api/disciplina/<idx>', methods=['PATCH'])
@jwt_required
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

    try:
        data = request.get_json()
        dis = ctrl_disciplina.update_disciplina(idx, data)
        return jsonify(
            status=200,
            data=dis
        )
    except ExceptionDisciplinaNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )


@app_disciplina.route('/api/disciplina/<idx>', methods=['DELETE'])
@jwt_required
def delete_disciplina(idx):
    """
    @api {delete} /api/disciplina/:id Deleta disciplina
    @apiVersion 1.0.0-a
    @apiName DeleteDisciplina
    @apiGroup Disciplina

    @apiDescription Deleta um <code>Disciplina</code> existente

    @apiUse DisciplinaNotFoundError
    """

    try:
        data = request.get_json()
        dis = ctrl_disciplina.delete_disciplina(idx)
        return jsonify(
            status=200,
            data=dis
        )
    except ExceptionDisciplinaNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )