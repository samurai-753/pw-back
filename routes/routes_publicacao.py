from flask import Blueprint, jsonify


app_publicacao = Blueprint('publicacao', __name__)


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
        data={}
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

    return jsonify(
        status=200,
        data={}
    )


@app_publicacao.route('/api/publicacao', methods=['POST'])
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

    return jsonify(
        status=200,
        data={}
    )


@app_publicacao.route('/api/publicacao/<idx>', methods=['PATCH'])
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

    return jsonify(
        status=200,
        data={}
    )


@app_publicacao.route('/api/publicacao/<idx>', methods=['DELETE'])
def delete_publicacao(idx):
    """
    @api {delete} /api/publicacao/:id Deleta Publicação
    @apiVersion 1.0.0-a
    @apiName DeletePublicacao
    @apiGroup Publicacao

    @apiDescription Deleta uma <code>Publicacao</code> existente

    @apiUse PublicacaoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )