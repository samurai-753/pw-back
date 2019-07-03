from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controller import CtrlPublicacao
from exception import ExceptionPublicacaoCampoInvalido, ExceptionPublicacaoNaoEncontrado


app_publicacao = Blueprint('publicacao', __name__)
ctrl_publicacao = CtrlPublicacao()


@app_publicacao.route('/api/publicacao', methods=['GET'])
def get_publicacao():
    """
    @api {get} /api/publicacao Recupera Publicações
    @apiVersion 1.0.0-a
    @apiName GetPublicacoes
    @apiGroup Publicacao

    @apiDescription Recupera a lista de todas as Publicações castradas no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>Publicacao</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx" = 206
                    "info" = ""
                    "publicacao" = ""
                    "tipo_publicacao" = "RES"
                }, {
                    ...
                }
            ]
        }
    """

    return jsonify(
        status=200,
        data=ctrl_publicacao.get_publicacacoes()
    )


@app_publicacao.route('/api/publicacao/<idx>', methods=['GET'])
def get_publicacao_idx(idx):
    """
    @api {get} /api/publicacao/:id Recupera Publicação
    @apiVersion 1.0.0-a
    @apiName GetPublicacaoId
    @apiGroup Publicacao

    @apiDescription Recupera a publicacao com o <code>id</code> fornecido

    @apiUse PublicacaoExemplo

    @apiUse PublicacaoNotFoundError
    """

    pub = ctrl_publicacao.get_publicacao(idx)
    if pub:
        return jsonify(
            status=200,
            data=pub
        )
    else:
        e = ExceptionPublicacaoNaoEncontrado('idx', idx)
        return jsonify(
            status=404,
            message=str(e)
        )


@app_publicacao.route('/api/publicacao', methods=['POST'])
@jwt_required
def post_publicacao():
    """
    @api {post} /api/publicacao/ Adiciona Publicação
    @apiVersion 1.0.0-a
    @apiName PostPublicacao
    @apiGroup Publicacao

    @apiDescription Adiciona uma nova <code>Publicacao</code>

    @apiUse ObjetoPublicacao

    @apiUse PublicacaoExemplo
    """

    try:
        data = request.get_json()
        publicacao = ctrl_publicacao.add_publicacao(data)

        return jsonify(
            status=200,
            data=publicacao
        )
    except ExceptionPublicacaoCampoInvalido as e:
        return jsonify(
            status=400,
            message=str(e)
        )


@app_publicacao.route('/api/publicacao/<idx>', methods=['PATCH'])
@jwt_required
def update_publicacao(idx):
    """
    @api {patch} /api/publicacao/:id Atualiza Publicação
    @apiVersion 1.0.0-a
    @apiName PutPublicacao
    @apiGroup Publicacao

    @apiDescription Atualiza uma <code>Publicacao</code> existente

    @apiUse ObjetoPublicacaoMod

    @apiUse PublicacaoNotFoundError
    """

    try:
        data = request.get_json()
        publicacao = ctrl_publicacao.update_publicacao(idx, data)

        return jsonify(
            status=200,
            data=publicacao
        )
    except ExceptionPublicacaoNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )


@app_publicacao.route('/api/publicacao/<idx>', methods=['DELETE'])
@jwt_required
def delete_publicacao(idx):
    """
    @api {delete} /api/publicacao/:id Deleta Publicação
    @apiVersion 1.0.0-a
    @apiName DeletePublicacao
    @apiGroup Publicacao

    @apiDescription Deleta uma <code>Publicacao</code> existente

    @apiUse PublicacaoNotFoundError
    """

    try:
        ctrl_publicacao.delete_publicacao(idx)
        return jsonify(
            status=200,
            data={}
        )
    except ExceptionPublicacaoNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )