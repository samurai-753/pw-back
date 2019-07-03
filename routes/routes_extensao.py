from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controller import CtrlExtensao
from exception import ExceptionExtensaoCampoInvalido, ExceptionExtensaoNaoEncontrado


app_extensao = Blueprint('extensao', __name__)
ctrl_extensao = CtrlExtensao()


@app_extensao.route('/api/extensao', methods=['GET'])
def get_extensao():
    """
    @api {get} /api/extensao Recupera Extensões
    @apiVersion 1.0.0-a
    @apiName GetExtensoes
    @apiGroup Extensao

    @apiDescription Recupera a lista de todos os Extensões castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>Extensao</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx" = 520,
                    "inicio" = "2018-07-01",
                    "fim" = "2019-06-30",
                    "tipo_extensao" = "",
                    "documento" = "3",
                }, {
                    ...
                }
            ]
        }
    """

    return jsonify(
        status=200,
        data=ctrl_extensao.get_extensoes()
    )


@app_extensao.route('/api/extensao/<idx>', methods=['GET'])
def get_extensao_idx(idx):
    """
    @api {get} /api/extensao/:id Recupera Extensao
    @apiVersion 1.0.0-a
    @apiName GetExtensaoId
    @apiGroup Extensao

    @apiDescription Recupera a extensao com o <code>id</code> fornecido

    @apiUse ExtensaoExemplo

    @apiUse ExtensaoNotFoundError
    """

    ext = ctrl_extensao.get_extensao(int(idx))
    if ext:
        return jsonify(
            status=200,
            data=ext
        )
    else:
        e = ExceptionExtensaoNaoEncontrado('idx', idx)
        return jsonify(
            status=404,
            message=str(e)
        )


@app_extensao.route('/api/extensao', methods=['POST'])
@jwt_required
def post_extensao():
    """
    @api {post} /api/extensao/ Adiciona Extensao
    @apiVersion 1.0.0-a
    @apiName PostExtensao
    @apiGroup Extensao

    @apiDescription Adiciona uma nova <code>Extensao</code>

    @apiUse ObjetoExtensao

    @apiUse ExtensaoExemplo
    """

    data = request.get_json()

    try:
        extensao = ctrl_extensao.add_extensao(data)
        return jsonify(
            status=200,
            data=extensao
        )
    except ExceptionExtensaoCampoInvalido as e:
        return jsonify(
            status=400,
            message=str(e)
        )


@app_extensao.route('/api/extensao/<idx>', methods=['PATCH'])
@jwt_required
def update_extensao(idx):
    """
    @api {patch} /api/extensao/:id Atualiza Extensao
    @apiVersion 1.0.0-a
    @apiName PutExtensao
    @apiGroup Extensao

    @apiDescription Atualiza uma <code>Extensao</code> existente

    @apiUse ObjetoExtensaoMod

    @apiUse ExtensaoNotFoundError
    """

    data = request.get_json()

    try:
        ext = ctrl_extensao.update_extensao(idx, data)
        return jsonify(
            status=200,
            data=ext
        )
    except ExceptionExtensaoNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )


@app_extensao.route('/api/extensao/<idx>', methods=['DELETE'])
@jwt_required
def delete_extensao(idx):
    """
    @api {delete} /api/extensao/:id Deleta Extensao
    @apiVersion 1.0.0-a
    @apiName DeleteExtensao
    @apiGroup Extensao

    @apiDescription Deleta uma <code>Extensao</code> existente

    @apiUse ExtensaoNotFoundError
    """

    try:
        ctrl_extensao.delete_extensao(idx)
        return jsonify(
            status=200,
        )
    except ExceptionExtensaoNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )