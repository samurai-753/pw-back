from app import app
from routes import *


app.register_blueprint(app_main)
app.register_blueprint(app_professor)
app.register_blueprint(app_aluno)
app.register_blueprint(app_extensao)
app.register_blueprint(app_documento)
app.register_blueprint(app_publicacao)
app.register_blueprint(app_disciplina)
app.register_blueprint(app_projeto)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)