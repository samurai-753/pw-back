# pw-back

Backend do trabalho prático da disciplina de Programação Web, consiste de uma API REST para o frontend do mesmo projeto.

## Modo de utilizar

Após clonar o repositório instale as dependências usando o comando:

```
pipenv install
```

Por padrão, a aplicação utiliza um banco de dados SQLite3 local, para usar outro banco de dados relacional SQL crie uma variável de ambiente com nome `DB_URI`, por exemplo usando o shell do Linux:
```
export DB_URI="mysql+pymysql://myuser:pass@example.com:3306/database"
```

Para criar as tableas na primeira execução execute o segundo comando
```
pipenv shell
python3 -c "import app; impot model; app.db.create_all()"
```

Para executar os teste localmente use o comando
```
pipenv shell
nose2
```

Para executar a aplição execute o comando:
```
pipenv shell
python3 app.py
```

## Padrões do projeto

### Padrão do Git
- **Nunca faça um commit na master**
- Para cada nova feature crie um novo branch apartir da master
- Crie um Pull Request para poder dar merge na master
- Mantenha os branches locais atualizado
- Use nomes descritivos nos commits ("Adiciona rota POST /professor")
- Use uma referência das issues
- Coloque uma lista de mudanças no commit

### Padrão de código
- Siga a [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Sempre faça a documentação das rotas
- Mantenha as pastas organizadas

