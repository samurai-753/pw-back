from model.professor import Professor
from pprint import pprint

class CtrlProfessor:

    def __init__(self):
        self.professores = [
            Professor(1, 'Dudu', 'dudu@samurai.io', '(99) 123-123', 'dcc-01', ['bacharel','phd'])
        ]

    def get_professor(self, id_):
        p = [ x for x in self.professores if x.id ==  id_ ][0]
        return p