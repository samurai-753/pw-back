from flask import Blueprint, jsonify


app_aluno = Blueprint('aluno', __name__)


@app_aluno.route('/api/aluno', methods=['GET'])
def get_aluno():
    """
    @api {get} /api/aluno Recupera alunos
    @apiVersion 1.0.0-a
    @apiName GetAlunos
    @apiGroup Aluno

    @apiDescription Recupera a lista de todos os alunos castrados no
    sistema

    @apiSuccess {Number} code 200
    @apiSuccess {Object[]} data Lista de <code>Aluno</code>

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [
                {
                    "idx": 1,
                    "nome": "Gabriel Ribolive",
                    "email": "ribolive@dcc.ufla.br",
                    "telefone": "35912345678",
                    "resumo": "CA Computão 2016-2017, Bolsista FAPEMIG 2018"
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


@app_aluno.route('/api/aluno/<idx>', methods=['GET'])
def get_aluno_idx(idx):
    """
    @api {get} /api/aluno/:id Recupera aluno
    @apiVersion 1.0.0-a
    @apiName GetAlunoId
    @apiGroup Aluno

    @apiDescription Recupera o aluno com o <code>id</code> fornecido

    @apiUse AlunoExemplo

    @apiUse AlunoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_aluno.route('/api/aluno', methods=['POST'])
def post_aluno():
    """
    @api {post} /api/aluno/:id Adiciona aluno
    @apiVersion 1.0.0-a
    @apiName PostAluno
    @apiGroup Aluno

    @apiDescription Adiciona um novo <code>Aluno</code>

    @apiUse ObjetoPessoa
    @apiUse ObjetoAluno

    @apiUse AlunoExemplo
    """

    return jsonify(
        status=200,
        data={}
    )


@app_aluno.route('/api/aluno/<idx>', methods=['PUT'])
def update_aluno(idx):
    """
    @api {put} /api/aluno/:id Atualiza aluno
    @apiVersion 1.0.0-a
    @apiName PutAluno
    @apiGroup Aluno

    @apiDescription Atualiza um <code>Aluno</code> existente

    @apiUse ObjetoPessoaMod
    @apiUse ObjetoAlunoMod

    @apiUse AlunoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )


@app_aluno.route('/api/aluno/<idx>', methods=['DELETE'])
def delete_aluno(idx):
    """
    @api {delete} /api/aluno/:id Deleta aluno
    @apiVersion 1.0.0-a
    @apiName DeleteAluno
    @apiGroup Aluno

    @apiDescription Deleta um <code>Aluno</code> existente

    @apiUse ObjetoPessoaMod
    @apiUse ObjetoAlunoMod

    @apiUse AlunoNotFoundError
    """

    return jsonify(
        status=200,
        data={}
    )