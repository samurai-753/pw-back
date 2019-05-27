define({ "api": [
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [{\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        ...\n    }, {\n        ...\n    }]\n}",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        ...\n    }\n}",
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
    "title": "Novo professor",
    "version": "1.0.0-a",
    "name": "PostProfessor",
    "group": "Professor",
    "description": "<p>Post um novo professor</p>",
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
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"idx\": 1,\n        \"nome\": \"Durelli\",\n        \"email\": \"durelli@dcc.ufla.br\",\n        ...\n    }\n}",
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
