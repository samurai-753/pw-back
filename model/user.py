from app import db


class User(db.Model):
    email = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # professor = db.Column(db.Boolean)
    # admin = db.Column(db.Boolean)

    # pessoa_idx = db.Column(
    #     db.Integer, db.ForeignKey('pessoa.idx'), nullable=True
    # )
    # pessoa = db.relationship('Pessoa', uselist=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        # self.pessoa_idx = pessoa_idx
        # self.professor = professor
        # self.admin = admin
    
    def check_password(self, password):
        return self.password == password
