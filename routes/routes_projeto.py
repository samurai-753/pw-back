from flask import Blueprint, jsonify, request
from controller import CtrlProjeto
from exception import ExceptionProjetoCampoInvalido, ExceptionProjetoNaoEncontrado


app_projeto = Blueprint('projeto', __name__)
ctrl_projeto = CtrlProjeto()

@app_projeto.errorhandler(ExceptionProjetoNaoEncontrado)
def handle_nao_encontrado(e):
    return jsonify(
        status=404,
        message=str(e)
    )

@app_projeto.errorhandler(ExceptionProjetoCampoInvalido)
def handle_campo_invalido(e):
    return jsonify(
            status=400,
            message=str(e)
    )


@app_projeto.route('/api/projeto', methods=['GET'])
def get_projeto():
    """
    @api {get} /api/projeto Recupera Projetos de pesquisas
    @apiVersion 1.0.0-a
    @apiName GetProjetos
    @apiGroup Projeto

    @apiDescription Recupera a lista de todos os Projetos de pesquisas castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>Projeto</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx": 485,
                    "nome" = "Aplicando o TSP para problema de roteamento de veículos",
                    "orientador" = 2134,
                    "coorientador" = 134,
                    "alunos" = [22, 545],
                }, {
                    ...
                }
            ]
        }
    """

    return jsonify(
        status=200,
        data=ctrl_projeto.get_projetos()
    )


@app_projeto.route('/api/projeto/<idx>', methods=['GET'])
def get_projeto_idx(idx):
    """
    @api {get} /api/projeto/:id Recupera Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName GetProjetoId
    @apiGroup Projeto

    @apiDescription Recupera o documento com o <code>id</code> fornecido

    @apiUse ProjetoExemplo

    @apiUse ProjetoNotFoundError
    """

    return jsonify(
        status=200,
        data=ctrl_projeto.get_projeto(idx)
    )


@app_projeto.route('/api/projeto', methods=['POST'])
def post_projeto():
    """
    @api {post} /api/projeto/ Adiciona Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName PostProjeto
    @apiGroup Projeto

    @apiDescription Adiciona um novo <code>Projeto</code>

    @apiUse ObjetoProjeto

    @apiUse ProjetoExemplo
    """

    data = request.get_json()
    proj = ctrl_projeto.add_projeto(data)

    return jsonify(
        status=200,
        data=proj
    )
        


@app_projeto.route('/api/projeto/<idx>', methods=['PATCH'])
def update_projeto(idx):
    """
    @api {patch} /api/projeto/:id Atualiza Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName PutProjeto
    @apiGroup Projeto

    @apiDescription Atualiza um <code>Projeto</code> existente

    @apiUse ObjetoProjetoMod

    @apiUse ProjetoNotFoundError
    """

    data = request.get_json()
    proj = ctrl_projeto.update_projeto(idx, data)

    return jsonify(
        status=200,
        data=proj
    )


@app_projeto.route('/api/projeto/<idx>', methods=['DELETE'])
def delete_projeto(idx):
    """
    @api {delete} /api/projeto/:id Deleta Projeto de pesquisa
    @apiVersion 1.0.0-a
    @apiName DeleteProjeto
    @apiGroup Projeto

    @apiDescription Deleta um <code>Projeto</code> existente

    @apiUse ProjetoNotFoundError
    """

    return jsonify(
        status=200,
        data=ctrl_projeto.delete_projeto(idx)
    )