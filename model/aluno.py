from app import db


class Aluno(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    detalhes_idx = db.Column(
        db.Integer, db.ForeignKey('pessoa.idx'), nullable=False
    )
    detalhes = db.relationship('Pessoa', uselist=False)
    resumo = db.Column(db.Text)

    def __init__(self, detalhes_idx, idx=0, resumo=''):
        self.idx = idx
        self.detalhes_idx = detalhes_idx
        self.resumo = resumo

    def __repr__(self):
        return '<Aluno idx={} />'.format(self.idx)