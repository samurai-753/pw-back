from app import db
from .helpers import Disciplina_Documento


class Disciplina(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(4), nullable=False)

    professor_idx = db.Column(
        db.Integer, db.ForeignKey('professor.idx'), nullable=False
    )
    professor = db.relationship('Professor', uselist=False)

    documentos = db.relationship(
        'Documento', secondary=Disciplina_Documento, lazy='subquery'
    )

    def __init__(self, nome, tipo, professor_idx, idx=0, documentos=[]):
        self.idx = idx
        self.nome = nome
        self.tipo = tipo
        self.professor_idx = professor_idx
        self.documentos = documentos

    def __repr__(self):
        return '<Disciplina nome={} />'.format(self.nome)

