from flask import Blueprint, jsonify, request, send_from_directory, send_file
from controller import CtrlDocumento
from exception import ExceptionDocumentoNaoEncontrado
from app import UPLOAD_FOLDER


app_documento = Blueprint('documento', __name__)
ctrl_documento = CtrlDocumento()


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

    docs = ctrl_documento.get_documentos()
    return jsonify(
        status=200,
        data=docs
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

    doc = ctrl_documento.get_documento(idx)
    if doc:
        print(doc.name, doc.path)
        return send_file(doc.path, attachment_filename=doc.nome, as_attachment=True)
    else:
        e = ExceptionDocumentoNaoEncontrado('idx', idx)
        return jsonify(
            status=404,
            message=str(e)
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

    src_file = request.files['file']
    doc = ctrl_documento.add_documento(src_file)

    return jsonify(
        status=200,
        data=doc
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

    data = request.get_json()

    try:
        doc = ctrl_documento.update_documento(idx, data)
        return jsonify(
            status=200,
            data=doc
        )
    except ExceptionDocumentoNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
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

    try:
        ctrl_documento.delete_documento(idx)
        return jsonify(
            status=200,
        )
    except:
        e = ExceptionDocumentoNaoEncontrado('idx', idx)
        return jsonify(
            status=404,
            message=str(e)
        )