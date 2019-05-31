from flask import Blueprint, jsonify


app_projeto_pesquisa = Blueprint('projeto_pesquisa', __name__)


@app_projeto_pesquisa.route('/api/projeto_pesquisa', methods=['GET'])
def get_projeto_pesquisa():
    """
    @api {get} /api/projeto_pesquisa Recupera Projeto de pesquisas
    @apiVersion 1.0.0-a
    @apiName GetProjetoPesquisas
    @apiGroup ProjetoPesquisa

    @apiDescription Recupera a lista de todos os Projetos de pesquisas castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>ProjetoPesquisa</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx": 485,
                    "nome" = "Aplicando o TSP para problema de roteamento de veículos",
                    "orientador" = "Luis Carlos",
                    "coorientador" = "Paulo Vitor",
                    "alunos" = [Lucas Alves, Guilherme Oliveira],
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


@app_projeto_pesquisa.route('/api/projeto_pesquisa/<idx>', methods=['GET'])
def get_projeto_pesquisa_idx(idx):
    """
    @api {get} /api/projeto_pesquisa/:id Recupera Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName GetProjetoPesquisaId
    @apiGroup ProjetoPesquisa

    @apiDescription Recupera o aluni com o <code>id</code> fornecido

    @apiUse ProjetoPesquisaExemplo

    @apiUse ProjetoPesquisaNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_projeto_pesquisa.route('/api/projeto_pesquisa', methods=['POST'])
def post_projeto_pesquisa():
    """
    @api {post} /api/projeto_pesquisa/ Adiciona Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName PostProjetoPesquisa
    @apiGroup ProjetoPesquisa

    @apiDescription Adiciona um novo <code>ProjetoPesquisa</code>

    @apiUse ObjetoProjetoPesquisa

    @apiUse ProjetoPesquisaExemplo
    """

    return jsonify(
        status=200,
        data={}
    )


@app_projeto_pesquisa.route('/api/projeto_pesquisa/<idx>', methods=['PATCH'])
def update_projeto_pesquisa(idx):
    """
    @api {patch} /api/projeto_pesquisa/:id Atualiza Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName PutProjetoPesquisa
    @apiGroup ProjetoPesquisa

    @apiDescription Atualiza um <code>ProjetoPesquisa</code> existente

    @apiUse ObjetoProjetoPesquisaMod

    @apiUse ProjetoPesquisaNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_projeto_pesquisa.route('/api/projeto_pesquisa/<idx>', methods=['DELETE'])
def delete_projeto_pesquisa(idx):
    """
    @api {delete} /api/projeto_pesquisa/:id Deleta Projeto de Pesquisa
    @apiVersion 1.0.0-a
    @apiName DeleteProjetoPesquisa
    @apiGroup ProjetoPesquisa

    @apiDescription Deleta um <code>ProjetoPesquisa</code> existente

    @apiUse ProjetoPesquisaNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )