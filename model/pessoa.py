from app import db


class Pessoa(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefone = db.Column(db.String(12))

    def __init__(self, nome, email, idx=0, telefone=''):
        self.idx = idx
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Pessoa idx={} nome={} />'.format(self.idx, self.nome)