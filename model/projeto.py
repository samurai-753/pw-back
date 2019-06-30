from app import db
from .helpers import Projeto_Aluno


class Projeto(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False, unique=True)

    orientador_idx = db.Column(
        db.Integer, db.ForeignKey('professor.idx'), nullable=False
    )
    orientador = db.relationship('Professor', uselist=False)

    coorientador_idx = db.Column(
        db.Integer, db.ForeignKey('professor.idx'), nullable=True
    )
    coorientador = db.relationship('Professor', uselist=False)

    alunos = db.relationship(
        'Aluno', secondary=Projeto_Aluno, lazy='subquery'
    )

    def __init__(self, nome, orientador_idx, alunos=[], idx=0, coorientador_idx=None):
        self.idx = idx
        self.nome = nome
        self.orientador_idx = orientador_idx
        self.coorientador_idx = coorientador_idx
        self.alunos = alunos
    
    def __repr__(self):    
        return '<ProjeotPesquisa idx={} nome={} {}/>'.format(
            self.idx, self.nome
        )

