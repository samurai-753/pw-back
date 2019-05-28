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
            "optional": false,
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
            "optional": false,
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
    "type": "put",
    "url": "/api/professor/:id",
    "title": "Atualiza professor",
    "version": "1.0.0-a",
    "name": "PutProfessor",
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
