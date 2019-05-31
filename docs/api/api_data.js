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
    "description": "<p>Recupera o aluni com o <code>id</code> fornecido</p>",
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
    "description": "<p>Recupera o aluni com o <code>id</code> fornecido</p>",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 1,\n            \"nome\": \"Durelli\",\n            \"email\": \"durelli@dcc.ufla.br\",\n            \"telefone\": \"35912345678\",\n            \"sala\": \"DCC26\",\n            \"extensões\": [\n                \"Bacharel e ciência da computção, UFLA 2007\"\n            ]\n        }, {\n            ...\n        }\n    ]\n}",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        \"telefone\": \"35912345678\",\n        \"sala\": \"DCC26\",\n        \"extensões\": [\n            \"Bacharel e ciência da computção, UFLA 2007\"\n        ]\n    }\n}",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        \"telefone\": \"35912345678\",\n        \"sala\": \"DCC26\",\n        \"extensões\": [\n            \"Bacharel e ciência da computção, UFLA 2007\"\n        ]\n    }\n}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "delete",
    "url": "/api/projeto_pesquisa/:id",
    "title": "Deleta Projeto de Pesquisa",
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
    "description": "<p>Recupera o aluni com o <code>id</code> fornecido</p>",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 485,\n    \"nome\" = \"Aplicando o TSP para problema de roteamento de veículos\",\n    \"orientador\" = \"Luis Carlos\",\n    \"coorientador\" = \"Paulo Vitor\",\n    \"alunos\" = [Lucas Alves, Guilherme Oliveira],\n}",
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
    "title": "Recupera Projeto de pesquisas",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [\n        {\n            \"idx\": 485,\n            \"nome\" = \"Aplicando o TSP para problema de roteamento de veículos\",\n            \"orientador\" = \"Luis Carlos\",\n            \"coorientador\" = \"Paulo Vitor\",\n            \"alunos\" = [Lucas Alves, Guilherme Oliveira],\n        }, {\n            ...\n        }\n    ]\n}",
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
            "description": "<p><code>idx</code> do professor</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome_projeto_pesquisa",
            "description": "<p>Nome do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome_orientador",
            "description": "<p>Nome do orientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome_coorientador",
            "description": "<p>Nome do coorientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "String[]",
            "optional": false,
            "field": "nome_alunos",
            "description": "<p>Nome dos alunos do projeto de pesquisa</p>"
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
          "content": "HTTP/1.1 200 OK\n{\n    \"idx\": 485,\n    \"nome\" = \"Aplicando o TSP para problema de roteamento de veículos\",\n    \"orientador\" = \"Luis Carlos\",\n    \"coorientador\" = \"Paulo Vitor\",\n    \"alunos\" = [Lucas Alves, Guilherme Oliveira],\n}",
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
            "type": "String",
            "optional": false,
            "field": "nome_projeto_pesquisa",
            "description": "<p>Nome do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome_orientador",
            "description": "<p>Nome do orientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "nome_coorientador",
            "description": "<p>Nome do coorientador do projeto de pesquisa</p>"
          },
          {
            "group": "Parameter",
            "type": "String[]",
            "optional": false,
            "field": "nome_alunos",
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
    "group": "_home_thuza_Documents_Periodo_7_PROG_WEB_pw_back_docs_api_main_js",
    "groupTitle": "_home_thuza_Documents_Periodo_7_PROG_WEB_pw_back_docs_api_main_js",
    "name": ""
  }
] });
