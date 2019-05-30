from app import db


class Professor(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    detalhes_idx = db.Column(
        db.Integer, db.ForeignKey('pessoa.idx'), nullable=False
    )
    sala = db.Column(db.String(5), nullable=False)

    def __init__(self, detalhes_idx, sala, idx=0):
        self.idx = idx
        self.detalhes_idx = detalhes_idx
        self.sala = sala

    def __repr__(self):
        return '<Professor idx={} nome={} />'.format(self.idx, self.nome)