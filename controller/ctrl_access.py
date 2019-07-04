from app import db
from model import User


class CtrlAccess():

    def __init__(self):
        self.session = db.session

    def get_user(self, email):
        return User.query.filter_by(email=email).first()