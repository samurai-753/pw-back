from app import db


class User(db.Model):
    email = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean)

    professor_idx = db.Column(
        db.Integer, db.ForeignKey('professor.idx'), nullable=True
    )
    professor = db.relationship('Professor', uselist=False)

    def __init__(self, email, password, professor_idx):
        self.email = email
        self.password = password
        self.admin = False
        self.professor_idx = professor_idx
    
    def check_password(self, password):
        return self.password == password
