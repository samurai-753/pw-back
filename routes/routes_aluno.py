from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controller import CtrlAluno, CtrlPessoa
from model import Aluno, Pessoa
from pprint import pprint
from exception import ExceptionAlunoNaoEncontrado, ExceptionAlunoCampoInvalido


app_aluno = Blueprint('aluno', __name__)
ctrl_aluno = CtrlAluno()
ctrl_pessoa = CtrlPessoa()


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
        data=ctrl_aluno.get_alunos()
    )


@app_aluno.route('/api/aluno/<idx>', methods=['GET'])
def get_aluno_idx(idx):
    """
    @api {get} /api/aluno/:idx Recupera aluno
    @apiVersion 1.0.0-a
    @apiName GetAlunoId
    @apiGroup Aluno

    @apiDescription Recupera o aluno com o <code>id</code> fornecido

    @apiUse AlunoExemplo

    @apiUse AlunoNotFoundError
    """

    a = ctrl_aluno.get_aluno(idx)
    if a:
        return jsonify(
            status=200,
            data=a
        )
    else:
        e = ExceptionAlunoNaoEncontrado('idx', idx)
        return jsonify(
            status=404,
            message=str(e)
        )


@app_aluno.route('/api/aluno', methods=['POST'])
# @jwt_required
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

    try:
        data = request.get_json()
        aluno = ctrl_aluno.add_aluno(data)

        return jsonify(
            status=200,
            data=aluno
        )
    
    except KeyError as ke:
        e = ExceptionAlunoCampoInvalido(ke)
        return jsonify(
            status=400,
            message=str(e)
        )


@app_aluno.route('/api/aluno/<idx>', methods=['PATCH'])
# @jwt_required
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

    try:
        data = request.get_json()
        
        nome = data.get('nome')
        email = data.get('email')
        telefone = data.get('telefone')
        resumo = data.get('resumo')

        aluno_dict = ctrl_aluno.update_aluno(idx, nome, email, telefone, resumo)

        return jsonify(
            status=200,
            data=aluno_dict
        )
            
    except ExceptionAlunoNaoEncontrado as e:
        return jsonify(
            status=404,
            message=str(e)
        )


@app_aluno.route('/api/aluno/<idx>', methods=['DELETE'])
# @jwt_required
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

    try:
        ctrl_aluno.delete_aluno(idx)
        return jsonify(
            status=200,
            data={}
        )
    except:
        e = ExceptionAlunoNaoEncontrado('idx', idx) 
        return jsonify(
            status=404,
            message=str(e)
        )