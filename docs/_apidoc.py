"""
@apiDefine ProfessorNotFoundError

@apiError {ProfessorNotFound} message  <code>professor</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "ProfessorNotFound"
    }
"""

"""
@apiDefine ProfessorExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>professor</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": {
                "idx": 1,
                "nome": "Durelli",
                "email": "durelli@dcc.ufla.br",
                ...
            }
        }
"""

"""
@apiDefine ObjetoPessoa

@apiParam {String} nome Nome da pessoa
@apiParam {String} email Email da pessoa
@apiParam {String} telefone Telefone da pessoa
"""

"""
@apiDefine ObjetoProfessor

@apiParam {String} sala Sala do professor
@apiParam {Object[]} titulos Titulos do professor
"""

"""
@apiDefine ObjetoPessoaMod

@apiParam {String} [nome] Nome da pessoa
@apiParam {String} [telefone] Telefone da pessoa
"""

"""
@apiDefine ObjetoProfessorMod

@apiParam {String} [sala] Sala do professor
@apiParam {Object[]} [titulos] Titulos do professor
"""