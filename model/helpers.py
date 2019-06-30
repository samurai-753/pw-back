from app import db


Disciplina_Documento = db.Table(
    'disciplina_documentos',
    db.Column('disciplina_idx', db.Integer, db.ForeignKey('disciplina.idx'), primary_key=True),
    db.Column('documento_idx', db.Integer, db.ForeignKey('documento.idx'), primary_key=True)
)

Extensao_Publicaco = db.Table(
    'extensao_publicaco',
    db.Column('extensao_idx', db.Integer, db.ForeignKey('extensao.idx'), primary_key=True),
    db.Column('publicacao_idx', db.Integer, db.ForeignKey('publicacao.idx'), primary_key=True)
)

Projeto_Aluno = db.Table(
    'projeto_aluno',
    db.Column('projeto_idx', db.Integer, db.ForeignKey('projeto.idx'), primary_key=True),
    db.Column('aluno_idx', db.Integer, db.ForeignKey('aluno.idx'), primary_key=True)
)