from app import db


class Documento(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False, unique=True)
    path = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, nome, path, idx=0):
        self.idx = idx
        self.nome = nome
        self.path = path
    
    def __repr__(self):
        return '<Documento idx={} />'.format(self.idx)