from flask import Blueprint, jsonify


app_documento = Blueprint('documento', __name__)


@app_documento.route('/api/documento', methods=['GET'])
def get_documento():
    """
    @api {get} /api/documento Recupera Documentos
    @apiVersion 1.0.0-a
    @apiName GetDocumentos
    @apiGroup Documento

    @apiDescription Recupera a lista de todos os Documentos castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>Documento</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx": 107,
                    "nome" = "TCC_Lucas.pdf",
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


@app_documento.route('/api/documento/<idx>', methods=['GET'])
def get_documento_idx(idx):
    """
    @api {get} /api/documento/:id Recupera Documento
    @apiVersion 1.0.0-a
    @apiName GetDocumentoId
    @apiGroup Documento

    @apiDescription Recupera o documento com o <code>id</code> fornecido

    @apiUse DocumentoExemplo

    @apiUse DocumentoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_documento.route('/api/documento', methods=['POST'])
def post_documento():
    """
    @api {post} /api/documento/ Adiciona Documento
    @apiVersion 1.0.0-a
    @apiName PostDocumento
    @apiGroup Documento

    @apiDescription Adiciona um novo <code>Documento</code>

    @apiUse ObjetoDocumento

    @apiUse DocumentoExemplo
    """

    return jsonify(
        status=200,
        data={}
    )


@app_documento.route('/api/documento/<idx>', methods=['PATCH'])
def update_documento(idx):
    """
    @api {patch} /api/documento/:id Atualiza Documento
    @apiVersion 1.0.0-a
    @apiName PutDocumento
    @apiGroup Documento

    @apiDescription Atualiza um <code>Documento</code> existente

    @apiUse ObjetoDocumentoMod

    @apiUse DocumentoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_documento.route('/api/documento/<idx>', methods=['DELETE'])
def delete_documento(idx):
    """
    @api {delete} /api/documento/:id Deleta Projeto de Pesquisa
    @apiVersion 1.0.0-a
    @apiName DeleteDocumento
    @apiGroup Documento

    @apiDescription Deleta um <code>Documento</code> existente

    @apiUse DocumentoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )