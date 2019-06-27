from app import db


class Documento(db.Model):
    idx = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, path, idx=0):
        self.idx = idx
        self.path = path
    
    def __repr__(self):
        return '<Documento idx={} />'.format(self.idx)