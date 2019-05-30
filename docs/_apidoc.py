# ============================================================================
# Pessoa
# ============================================================================

"""
@apiDefine ObjetoPessoa

@apiParam {String} nome Nome da pessoa
@apiParam {String} email Email da pessoa
@apiParam {String} [telefone] Telefone da pessoa
"""

"""
@apiDefine ObjetoPessoaMod

@apiParam {String} [nome] Nome da pessoa
@apiParam {String} [telefone] Telefone da pessoa
"""

# ============================================================================
# Professor
# ============================================================================

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
                "telefone": "35912345678",
                "sala": "DCC26",
                "extensões": [
                    "Bacharel e ciência da computção, UFLA 2007"
                ]
            }
        }
"""

"""
@apiDefine ObjetoProfessor

@apiParam {String} sala Sala do professor
@apiParam {Object[]} titulos Titulos do professor
"""

"""
@apiDefine ObjetoProfessorMod

@apiParam {String} [sala] Sala do professor
@apiParam {Object[]} [titulos] Titulos do professor
"""

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

# ============================================================================
# Aluno
# ============================================================================

"""
@apiDefine AlunoExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>aluno</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "idx": 1,
            "nome": "Gabriel Ribolive",
            "email": "ribolive@dcc.ufla.br",
            "telefone": "35912345678",
            "resumo": "CA Computão 2016-2017, Bolsista FAPEMIG 2018"
        }
"""

"""
@apiDefine ObjetoAluno

@apiParam {String} resumo Resumo do aluno
"""

"""
@apiDefine ObjetoAlunoMod

@apiParam {String} [sala] Resumo do aluno
"""

"""
@apiDefine AlunoNotFoundError

@apiError {AlunoNotFound} message  <code>Aluno</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "AlunoNotFound"
    }
"""