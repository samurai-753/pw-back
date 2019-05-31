from flask import Blueprint, jsonify


app_extensao = Blueprint('extensao', __name__)


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
        data={}
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

    return jsonify(
        status=200,
        data={}
    )


@app_extensao.route('/api/extensao', methods=['POST'])
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

    return jsonify(
        status=200,
        data={}
    )


@app_extensao.route('/api/extensao/<idx>', methods=['PATCH'])
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

    return jsonify(
        status=200,
        data={}
    )


@app_extensao.route('/api/extensao/<idx>', methods=['DELETE'])
def delete_extensao(idx):
    """
    @api {delete} /api/extensao/:id Deleta Extensao
    @apiVersion 1.0.0-a
    @apiName DeleteExtensao
    @apiGroup Extensao

    @apiDescription Deleta uma <code>Extensao</code> existente

    @apiUse ExtensaoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )