from app import db


class Publicacao(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    documento_idx = db.Column(
        db.Integer, db.ForeignKey('documento.idx'), nullable=False
    )
    documento = db.relationship('Documento', uselist=False)

    def __init__(self, info, tipo, idx=0, documento_idx=0):
        self.idx = idx
        self.info = info
        self.tipo = tipo
        self.documento_idx = documento_idx 