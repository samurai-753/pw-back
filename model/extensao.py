from app import db
from .helpers import Extensao_Publicaco


class Extensao(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer, nullable=False)
    inicio = db.Column(db.String(10), nullable=False)
    fim = db.Column(db.String(10), nullable=False)

    pessoa_idx = db.Column(
        db.Integer, db.ForeignKey('pessoa.idx'), nullable=False
    )
    pessoa = db.relationship(
        'Pessoa', lazy=True, uselist=False
    )

    publicacoes = db.relationship(
        'Publicacao', secondary=Extensao_Publicaco, lazy='subquery'
    )

    def __init__(self, tipo, inicio, fim, pessoa_idx, idx=0, publicacoes=[]):
        self.idx = idx
        self.tipo = tipo
        self.inicio = inicio
        self.fim = fim
        self.pessoa_idx = pessoa_idx
        self.publicacoes = publicacoes

    def __repr__(self):
        return '<Extensao inicio={} fim={} />'.format(self.inicio, self.fim)

