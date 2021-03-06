define({ "api": [
  {
    "type": "delete",
    "url": "/api/aluno/:id",
    "title": "Deleta aluno",
    "version": "1.0.0-a",
    "name": "DeleteAluno",
    "group": "Aluno",
    "description": "<p>Deleta um <code>Aluno</code> existente</p>",
    "filename": "./routes/routes_aluno.py",
    "groupTitle": "Aluno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "nome",
            "description": "<p>Nome da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "telefone",
            "description": "<p>Telefone da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "sala",
            "description": "<p>Resumo do aluno</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "AlunoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Aluno</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"AlunoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/aluno/:id",
    "title": "Recupera aluno",
    "version": "1.0.0-a",
    "name": "GetAlunoId",
    "group": "Aluno",
    "description": "<p>Recupera o aluno com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_aluno.py",
    "groupTitle": "Aluno",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>aluno</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 1,\n    \"nome\": \"Gabriel Ribolive\",\n    \"email\": \"ribolive@dcc.ufla.br\",\n    \"telefone\": \"35912345678\",\n    \"resumo\": \"CA Computão 2016-2017, Bolsista FAPEMIG 2018\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "AlunoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Aluno</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"AlunoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/aluno",
    "title": "Recupera alunos",
    "version": "1.0.0-a",
    "name": "GetAlunos",
    "group": "Aluno",
    "description": "<p>Recupera a lista de todos os alunos castrados no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>Aluno</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 1,\n            \"nome\": \"Gabriel Ribolive\",\n            \"email\": \"ribolive@dcc.ufla.br\",\n            \"telefone\": \"35912345678\",\n            \"resumo\": \"CA Computão 2016-2017, Bolsista FAPEMIG 2018\"\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_aluno.py",
    "groupTitle": "Aluno"
  },
  {
    "type": "post",
    "url": "/api/aluno/:id",
    "title": "Adiciona aluno",
    "version": "1.0.0-a",
    "name": "PostAluno",
    "group": "Aluno",
    "description": "<p>Adiciona um novo <code>Aluno</code></p>",
    "filename": "./routes/routes_aluno.py",
    "groupTitle": "Aluno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "telefone",
            "description": "<p>Telefone da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "resumo",
            "description": "<p>Resumo do aluno</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>aluno</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 1,\n    \"nome\": \"Gabriel Ribolive\",\n    \"email\": \"ribolive@dcc.ufla.br\",\n    \"telefone\": \"35912345678\",\n    \"resumo\": \"CA Computão 2016-2017, Bolsista FAPEMIG 2018\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "put",
    "url": "/api/aluno/:id",
    "title": "Atualiza aluno",
    "version": "1.0.0-a",
    "name": "PutAluno",
    "group": "Aluno",
    "description": "<p>Atualiza um <code>Aluno</code> existente</p>",
    "filename": "./routes/routes_aluno.py",
    "groupTitle": "Aluno",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "nome",
            "description": "<p>Nome da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "telefone",
            "description": "<p>Telefone da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "sala",
            "description": "<p>Resumo do aluno</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "AlunoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Aluno</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"AlunoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/disciplina/:id",
    "title": "Deleta disciplina",
    "version": "1.0.0-a",
    "name": "DeleteDisciplina",
    "group": "Disciplina",
    "description": "<p>Deleta um <code>Disciplina</code> existente</p>",
    "filename": "./routes/routes_disciplina.py",
    "groupTitle": "Disciplina",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "DisciplinaNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Disciplina</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"DisciplinaNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/disciplina/:id",
    "title": "Recupera disciplina",
    "version": "1.0.0-a",
    "name": "GetDisciplinaId",
    "group": "Disciplina",
    "description": "<p>Recupera o aluno com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_disciplina.py",
    "groupTitle": "Disciplina",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Disciplina</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 485,\n    \"tipo_disciplia\": \"Graduação\",\n    \"idx_professor\": 2563,\n    \"idx_documento\": [ 45663, 45226 ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "DisciplinaNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Disciplina</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"DisciplinaNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/disciplina",
    "title": "Recupera disciplinas",
    "version": "1.0.0-a",
    "name": "GetDisciplinas",
    "group": "Disciplina",
    "description": "<p>Recupera a lista de todos os disciplinas castrados no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>Disciplina</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 485,\n            \"tipo_disciplia\": \"Graduação\",\n            \"idx_professor\": 2563,\n            \"idx_documento\": [ 45663, 45226 ]\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_disciplina.py",
    "groupTitle": "Disciplina"
  },
  {
    "type": "post",
    "url": "/api/disciplina/",
    "title": "Adiciona disciplina",
    "version": "1.0.0-a",
    "name": "PostDisciplina",
    "group": "Disciplina",
    "description": "<p>Adiciona um novo <code>Disciplina</code></p>",
    "filename": "./routes/routes_disciplina.py",
    "groupTitle": "Disciplina",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"GRAD\"",
              "\"POS\""
            ],
            "optional": false,
            "field": "tipo_disciplia",
            "description": "<p>Tipo da disciplia</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "idx_professor",
            "description": "<p><code>idx</code> do professor</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": true,
            "field": "idx_documento",
            "description": "<p>Lista de <code>idx</code> dos documentos da disciplia</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Disciplina</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 485,\n    \"tipo_disciplia\": \"Graduação\",\n    \"idx_professor\": 2563,\n    \"idx_documento\": [ 45663, 45226 ]\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/api/disciplina/:id",
    "title": "Atualiza disciplina",
    "version": "1.0.0-a",
    "name": "PutDisciplina",
    "group": "Disciplina",
    "description": "<p>Atualiza um <code>Disciplina</code> existente</p>",
    "filename": "./routes/routes_disciplina.py",
    "groupTitle": "Disciplina",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"GRAD\"",
              "\"POS\""
            ],
            "optional": true,
            "field": "tipo_disciplia",
            "description": "<p>Tipo da disciplia</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "idx_professor",
            "description": "<p><code>idx</code> do professor</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": true,
            "field": "idx_documento",
            "description": "<p>Lista de <code>idx</code> dos documentos da disciplia</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "DisciplinaNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Disciplina</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"DisciplinaNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/documento/:id",
    "title": "Deleta Projeto de Pesquisa",
    "version": "1.0.0-a",
    "name": "DeleteDocumento",
    "group": "Documento",
    "description": "<p>Deleta um <code>Documento</code> existente</p>",
    "filename": "./routes/routes_documento.py",
    "groupTitle": "Documento",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "DocumentoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Documento</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"DocumentoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/documento/:id",
    "title": "Recupera Documento",
    "version": "1.0.0-a",
    "name": "GetDocumentoId",
    "group": "Documento",
    "description": "<p>Recupera o documento com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_documento.py",
    "groupTitle": "Documento",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Documento</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 327,\n    \"nome\" = \"TCC_Lucas.pdf\",\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "DocumentoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Documento</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"DocumentoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/documento",
    "title": "Recupera Documentos",
    "version": "1.0.0-a",
    "name": "GetDocumentos",
    "group": "Documento",
    "description": "<p>Recupera a lista de todos os Documentos castrados no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>Documento</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 107,\n            \"nome\" = \"TCC_Lucas.pdf\",\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_documento.py",
    "groupTitle": "Documento"
  },
  {
    "type": "post",
    "url": "/api/documento/",
    "title": "Adiciona Documento",
    "version": "1.0.0-a",
    "name": "PostDocumento",
    "group": "Documento",
    "description": "<p>Adiciona um novo <code>Documento</code></p>",
    "filename": "./routes/routes_documento.py",
    "groupTitle": "Documento",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome_documento",
            "description": "<p>Nome do documento</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Documento</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 327,\n    \"nome\" = \"TCC_Lucas.pdf\",\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/api/documento/:id",
    "title": "Atualiza Documento",
    "version": "1.0.0-a",
    "name": "PutDocumento",
    "group": "Documento",
    "description": "<p>Atualiza um <code>Documento</code> existente</p>",
    "filename": "./routes/routes_documento.py",
    "groupTitle": "Documento",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "nome_documento",
            "description": "<p>Nome do documento</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "DocumentoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Documento</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"DocumentoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/extensao/:id",
    "title": "Deleta Extensao",
    "version": "1.0.0-a",
    "name": "DeleteExtensao",
    "group": "Extensao",
    "description": "<p>Deleta uma <code>Extensao</code> existente</p>",
    "filename": "./routes/routes_extensao.py",
    "groupTitle": "Extensao",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ExtensaoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Extensao</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ExtensaoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/extensao/:id",
    "title": "Recupera Extensao",
    "version": "1.0.0-a",
    "name": "GetExtensaoId",
    "group": "Extensao",
    "description": "<p>Recupera a extensao com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_extensao.py",
    "groupTitle": "Extensao",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Extensao</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\" = 520,\n    \"inicio\" = \"2018-07-01\",\n    \"fim\" = \"2019-06-30\",\n    \"tipo_extensao\" = \"IC\",\n    \"documento\" = \"3\",\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ExtensaoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Extensao</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ExtensaoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/extensao",
    "title": "Recupera Extensões",
    "version": "1.0.0-a",
    "name": "GetExtensoes",
    "group": "Extensao",
    "description": "<p>Recupera a lista de todos os Extensões castrados no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>Extensao</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\" = 520,\n            \"inicio\" = \"2018-07-01\",\n            \"fim\" = \"2019-06-30\",\n            \"tipo_extensao\" = \"\",\n            \"documento\" = \"3\",\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_extensao.py",
    "groupTitle": "Extensao"
  },
  {
    "type": "post",
    "url": "/api/extensao/",
    "title": "Adiciona Extensao",
    "version": "1.0.0-a",
    "name": "PostExtensao",
    "group": "Extensao",
    "description": "<p>Adiciona uma nova <code>Extensao</code></p>",
    "filename": "./routes/routes_extensao.py",
    "groupTitle": "Extensao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Date",
            "optional": false,
            "field": "inicio",
            "description": "<p>data de início da extensão</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": false,
            "field": "fim",
            "description": "<p>data de término da extensão</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"IC, MEST, DOC, PDOC\""
            ],
            "optional": false,
            "field": "tipo_extensao",
            "description": "<p>Tipo da extensão</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "documento",
            "description": "<p><code>idx</code> do documento referente a extensão</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Extensao</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\" = 520,\n    \"inicio\" = \"2018-07-01\",\n    \"fim\" = \"2019-06-30\",\n    \"tipo_extensao\" = \"IC\",\n    \"documento\" = \"3\",\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/api/extensao/:id",
    "title": "Atualiza Extensao",
    "version": "1.0.0-a",
    "name": "PutExtensao",
    "group": "Extensao",
    "description": "<p>Atualiza uma <code>Extensao</code> existente</p>",
    "filename": "./routes/routes_extensao.py",
    "groupTitle": "Extensao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "tipo_extensao",
            "description": "<p>Tipo da extensão</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": true,
            "field": "inicio",
            "description": "<p>data de início da extensão</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": true,
            "field": "fim",
            "description": "<p>data de término da extensão</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "documento",
            "description": "<p><code>idx</code> do documento referente a extensão</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ExtensaoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Extensao</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ExtensaoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/professor/:id",
    "title": "Deleta professor",
    "version": "1.0.0-a",
    "name": "DeleteProfessor",
    "group": "Professor",
    "description": "<p>Deleta um professor existente</p>",
    "filename": "./routes/routes_professor.py",
    "groupTitle": "Professor",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "nome",
            "description": "<p>Nome da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "telefone",
            "description": "<p>Telefone da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "sala",
            "description": "<p>Sala do professor</p>"
          },
          {
            "group": "Parameter",
            "type": "Object[]",
            "optional": true,
            "field": "titulos",
            "description": "<p>Titulos do professor</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ProfessorNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>professor</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ProfessorNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/professor",
    "title": "Recupera professores",
    "version": "1.0.0-a",
    "name": "GetProfessor",
    "group": "Professor",
    "description": "<p>Recupera a lista de todos os professores castrados no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>professor</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 1,\n            \"nome\": \"Durelli\",\n            \"email\": \"durelli@dcc.ufla.br\",\n            \"telefone\": \"35912345678\",\n            \"sala\": \"DCC26\",\n            \"extensões\": [\n                \"Bacharel e ciência da computção, UFLA 2007\"\n            ],\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_professor.py",
    "groupTitle": "Professor"
  },
  {
    "type": "get",
    "url": "/api/professor/:id",
    "title": "Recupera professor",
    "version": "1.0.0-a",
    "name": "GetProfessorId",
    "group": "Professor",
    "description": "<p>Recupera o professor com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_professor.py",
    "groupTitle": "Professor",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>professor</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        \"telefone\": \"35912345678\",\n        \"sala\": \"DCC26\",\n        \"extensões\": [\n            123, 5436,\n        ],\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ProfessorNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>professor</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ProfessorNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/api/professor/:id",
    "title": "Atualiza professor",
    "version": "1.0.0-a",
    "name": "PatchProfessor",
    "group": "Professor",
    "description": "<p>Atualiza um professor existente</p>",
    "filename": "./routes/routes_professor.py",
    "groupTitle": "Professor",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "nome",
            "description": "<p>Nome da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "telefone",
            "description": "<p>Telefone da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "sala",
            "description": "<p>Sala do professor</p>"
          },
          {
            "group": "Parameter",
            "type": "Object[]",
            "optional": true,
            "field": "titulos",
            "description": "<p>Titulos do professor</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ProfessorNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>professor</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ProfessorNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "post",
    "url": "/api/professor/:id",
    "title": "Adiciona professor",
    "version": "1.0.0-a",
    "name": "PostProfessor",
    "group": "Professor",
    "description": "<p>Adiciona um novo professor</p>",
    "filename": "./routes/routes_professor.py",
    "groupTitle": "Professor",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome",
            "description": "<p>Nome da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>Email da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "telefone",
            "description": "<p>Telefone da pessoa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "sala",
            "description": "<p>Sala do professor</p>"
          },
          {
            "group": "Parameter",
            "type": "Object[]",
            "optional": false,
            "field": "titulos",
            "description": "<p>Titulos do professor</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>professor</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        \"telefone\": \"35912345678\",\n        \"sala\": \"DCC26\",\n        \"extensões\": [\n            123, 5436,\n        ],\n    }\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/projeto_pesquisa/:id",
    "title": "Deleta Projeto de pesquisa",
    "version": "1.0.0-a",
    "name": "DeleteProjetoPesquisa",
    "group": "ProjetoPesquisa",
    "description": "<p>Deleta um <code>ProjetoPesquisa</code> existente</p>",
    "filename": "./routes/routes_projeto_pesquisa.py",
    "groupTitle": "ProjetoPesquisa",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ProjetoPesquisaNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>ProjetoPesquisa</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ProjetoPesquisaNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/projeto_pesquisa/:id",
    "title": "Recupera Projeto de pesquisa",
    "version": "1.0.0-a",
    "name": "GetProjetoPesquisaId",
    "group": "ProjetoPesquisa",
    "description": "<p>Recupera o documento com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_projeto_pesquisa.py",
    "groupTitle": "ProjetoPesquisa",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>ProjetoPesquisa</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 485,\n    \"nome\" = \"Aplicando o TSP para problema de roteamento de veículos\",\n    \"orientador\" = 2134,\n    \"coorientador\" = 134,\n    \"alunos\" = [22, 545],\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ProjetoPesquisaNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>ProjetoPesquisa</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ProjetoPesquisaNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/projeto_pesquisa",
    "title": "Recupera Projetos de pesquisas",
    "version": "1.0.0-a",
    "name": "GetProjetoPesquisas",
    "group": "ProjetoPesquisa",
    "description": "<p>Recupera a lista de todos os Projetos de pesquisas castrados no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>ProjetoPesquisa</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 485,\n            \"nome\" = \"Aplicando o TSP para problema de roteamento de veículos\",\n            \"orientador\" = 2134,\n            \"coorientador\" = 134,\n            \"alunos\" = [22, 545],\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_projeto_pesquisa.py",
    "groupTitle": "ProjetoPesquisa"
  },
  {
    "type": "post",
    "url": "/api/projeto_pesquisa/",
    "title": "Adiciona Projeto de pesquisa",
    "version": "1.0.0-a",
    "name": "PostProjetoPesquisa",
    "group": "ProjetoPesquisa",
    "description": "<p>Adiciona um novo <code>ProjetoPesquisa</code></p>",
    "filename": "./routes/routes_projeto_pesquisa.py",
    "groupTitle": "ProjetoPesquisa",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "idx_projeto_pesquisa",
            "description": "<p>Nome do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "idx_orientador",
            "description": "<p><code>idx</code> do orientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "idx_coorientador",
            "description": "<p><code>idx</code> do coorientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": false,
            "field": "idx_alunos",
            "description": "<p><code>idx</code> dos alunos do projeto de pesquisa</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>ProjetoPesquisa</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 485,\n    \"nome\" = \"Aplicando o TSP para problema de roteamento de veículos\",\n    \"orientador\" = 2134,\n    \"coorientador\" = 134,\n    \"alunos\" = [22, 545],\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/api/projeto_pesquisa/:id",
    "title": "Atualiza Projeto de pesquisa",
    "version": "1.0.0-a",
    "name": "PutProjetoPesquisa",
    "group": "ProjetoPesquisa",
    "description": "<p>Atualiza um <code>ProjetoPesquisa</code> existente</p>",
    "filename": "./routes/routes_projeto_pesquisa.py",
    "groupTitle": "ProjetoPesquisa",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "idx_projeto_pesquisa",
            "description": "<p>Nome do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "idx_orientador",
            "description": "<p>Nome do orientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "idx_coorientador",
            "description": "<p>Nome do coorientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": true,
            "field": "idx_alunos",
            "description": "<p>Nome dos alunos do projeto de pesquisa</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "ProjetoPesquisaNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>ProjetoPesquisa</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"ProjetoPesquisaNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/publicacao/:id",
    "title": "Deleta Publicação",
    "version": "1.0.0-a",
    "name": "DeletePublicacao",
    "group": "Publicacao",
    "description": "<p>Deleta uma <code>Publicacao</code> existente</p>",
    "filename": "./routes/routes_publicacao.py",
    "groupTitle": "Publicacao",
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "PublicacaoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Publicacao</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"PublicacaoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/publicacao/:id",
    "title": "Recupera Publicação",
    "version": "1.0.0-a",
    "name": "GetPublicacaoId",
    "group": "Publicacao",
    "description": "<p>Recupera a publicacao com o <code>id</code> fornecido</p>",
    "filename": "./routes/routes_publicacao.py",
    "groupTitle": "Publicacao",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Publicacao</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 327,\n    \"info\" = \"\"\n    \"documentos\" = []\n    \"tipo_publicacao\" = \"CON\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "PublicacaoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Publicacao</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"PublicacaoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "get",
    "url": "/api/publicacao",
    "title": "Recupera Publicações",
    "version": "1.0.0-a",
    "name": "GetPublicacoes",
    "group": "Publicacao",
    "description": "<p>Recupera a lista de todas as Publicações castradas no sistema</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "data",
            "description": "<p>Lista de <code>Publicacao</code></p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\" = 206\n            \"info\" = \"\"\n            \"publicacao\" = \"\"\n            \"tipo_publicacao\" = \"RES\"\n        }, {\n            ...\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/routes_publicacao.py",
    "groupTitle": "Publicacao"
  },
  {
    "type": "post",
    "url": "/api/publicacao/",
    "title": "Adiciona Publicação",
    "version": "1.0.0-a",
    "name": "PostPublicacao",
    "group": "Publicacao",
    "description": "<p>Adiciona uma nova <code>Publicacao</code></p>",
    "filename": "./routes/routes_publicacao.py",
    "groupTitle": "Publicacao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "info",
            "description": "<p>Informações sobre a publicação</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": false,
            "field": "documentos",
            "description": "<p><code>idx</code> dos documentos</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"CON, RES, PER\""
            ],
            "optional": false,
            "field": "tipo_publicacao",
            "description": "<p>Tipo da publicação</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p><code>Publicacao</code> com <code>id</code> fornecido</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 327,\n    \"info\" = \"\"\n    \"documentos\" = []\n    \"tipo_publicacao\" = \"CON\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "patch",
    "url": "/api/publicacao/:id",
    "title": "Atualiza Publicação",
    "version": "1.0.0-a",
    "name": "PutPublicacao",
    "group": "Publicacao",
    "description": "<p>Atualiza uma <code>Publicacao</code> existente</p>",
    "filename": "./routes/routes_publicacao.py",
    "groupTitle": "Publicacao",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "info",
            "description": "<p>Informações sobre a publicação</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": true,
            "field": "documentos",
            "description": "<p><code>idx</code> dos documentos</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "\"CON, RES, PER\""
            ],
            "optional": true,
            "field": "tipo_publicacao",
            "description": "<p>Tipo da publicação</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "PublicacaoNotFound",
            "optional": false,
            "field": "message",
            "description": "<p><code>Publicacao</code> com <code>id</code> fornecido não foi encontrado</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Ok\n{\n    \"code\": 404,\n    \"message\": \"PublicacaoNotFound\"\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./docs/api/main.js",
    "group": "_home_k4t0mono_projs_pw_back_docs_api_main_js",
    "groupTitle": "_home_k4t0mono_projs_pw_back_docs_api_main_js",
    "name": ""
  }
] });
