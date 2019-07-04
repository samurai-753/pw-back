from app import db
from model import User


class CtrlAccess():

    def __init__(self):
        self.session = db.session

    def verify(self, user, model, row):
        pass