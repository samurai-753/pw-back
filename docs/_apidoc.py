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
                    123, 5436,
                ],
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

# ============================================================================
# Disciplina
# ============================================================================

"""
@apiDefine DisciplinaExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>Disciplina</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "idx": 485,
            "tipo_disciplia": "Graduação",
            "idx_professor": 2563,
            "idx_documento": [ 45663, 45226 ]
        }
"""

"""
@apiDefine ObjetoDisciplina

@apiParam {String="GRAD","POS"} tipo_disciplia Tipo da disciplia
@apiParam {Number} idx_professor <code>idx</code> do professor
@apiParam {Number[]} [idx_documento] Lista de <code>idx</code> dos documentos da disciplia
"""

"""
@apiDefine ObjetoDisciplinaMod

@apiParam {String="GRAD","POS"} [tipo_disciplia] Tipo da disciplia
@apiParam {Number} [idx_professor] <code>idx</code> do professor
@apiParam {Number[]} [idx_documento] Lista de <code>idx</code> dos documentos da disciplia
"""

"""
@apiDefine DisciplinaNotFoundError

@apiError {DisciplinaNotFound} message  <code>Disciplina</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "DisciplinaNotFound"
    }
"""


# ============================================================================
# ProjetoPesquisa
# ============================================================================

"""
@apiDefine ProjetoPesquisaExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>ProjetoPesquisa</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "idx": 485,
            "nome" = "Aplicando o TSP para problema de roteamento de veículos",
            "orientador" = 2134,
            "coorientador" = 134,
            "alunos" = [22, 545],
        }
"""

"""
@apiDefine ObjetoProjetoPesquisa

@apiParam {Number} idx_projeto_pesquisa Nome do projeto de pesquisa
@apiParam {Number} idx_orientador <code>idx</code> do orientador do projeto de pesquisa
@apiParam {Number} idx_coorientador <code>idx</code> do coorientador do projeto de pesquisa
@apiParam {Number[]} idx_alunos <code>idx</code> dos alunos do projeto de pesquisa
"""

"""
@apiDefine ObjetoProjetoPesquisaMod

@apiParam {Number} [idx_projeto_pesquisa] Nome do projeto de pesquisa
@apiParam {Number} [idx_orientador] Nome do orientador do projeto de pesquisa
@apiParam {Number} [idx_coorientador] Nome do coorientador do projeto de pesquisa
@apiParam {Number[]} [idx_alunos] Nome dos alunos do projeto de pesquisa
"""

"""
@apiDefine ProjetoPesquisaNotFoundError

@apiError {ProjetoPesquisaNotFound} message  <code>ProjetoPesquisa</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "ProjetoPesquisaNotFound"
    }
"""


# ============================================================================
# Documento
# ============================================================================

"""
@apiDefine DocumentoExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>Documento</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "idx": 327,
            "nome" = "TCC_Lucas.pdf",
        }
"""

"""
@apiDefine ObjetoDocumento

@apiParam {String} nome_documento Nome do documento
"""

"""
@apiDefine ObjetoDocumentoMod

@apiParam {String} [nome_documento] Nome do documento
"""

"""
@apiDefine DocumentoNotFoundError

@apiError {DocumentoNotFound} message  <code>Documento</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "DocumentoNotFound"
    }
"""

# ============================================================================
# Publicacao
# ============================================================================

"""
@apiDefine PublicacaoExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>Publicacao</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "idx": 327,
            "info" = ""
            "documentos" = []
            "tipo_publicacao" = "CON"
        }
"""

"""
@apiDefine ObjetoPublicacao

@apiParam {String} info Informações sobre a publicação
@apiParam {Number[]} documentos <code>idx</code> dos documentos
@apiParam {String="CON, RES, PER"} tipo_publicacao Tipo da publicação
"""

"""
@apiDefine ObjetoPublicacaoMod

@apiParam {String} [info] Informações sobre a publicação
@apiParam {Number[]} [documentos] <code>idx</code> dos documentos
@apiParam {String="CON, RES, PER"} [tipo_publicacao] Tipo da publicação
"""

"""
@apiDefine PublicacaoNotFoundError

@apiError {PublicacaoNotFound} message  <code>Publicacao</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "PublicacaoNotFound"
    }
"""


# ============================================================================
# Extensao
# ============================================================================

"""
@apiDefine ExtensaoExemplo

@apiSuccess {Number} code 200
@apiSuccess {Object} data <code>Extensao</code> com <code>id</code> fornecido

@apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "idx" = 520,
            "inicio" = "2018-07-01",
            "fim" = "2019-06-30",
            "tipo_extensao" = "IC",
            "documento" = "3",
        }
"""

"""
@apiDefine ObjetoExtensao

@apiParam {Date} inicio data de início da extensão
@apiParam {Date} fim data de término da extensão
@apiParam {String="IC, MEST, DOC, PDOC"} tipo_extensao Tipo da extensão
@apiParam {Number} documento <code>idx</code> do documento referente a extensão
"""

"""
@apiDefine ObjetoExtensaoMod

@apiParam {String} [tipo_extensao] Tipo da extensão
@apiParam {Date} [inicio] data de início da extensão
@apiParam {Date} [fim] data de término da extensão
@apiParam {Number} [documento] <code>idx</code> do documento referente a extensão
"""

"""
@apiDefine ExtensaoNotFoundError

@apiError {ExtensaoNotFound} message  <code>Extensao</code> com <code>id</code>
fornecido não foi encontrado

@apiErrorExample Error-Response:
    HTTP/1.1 200 Ok
    {
        "code": 404,
        "message": "ExtensaoNotFound"
    }
"""