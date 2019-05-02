from model import Aluno
from pprint import pprint

class CtrlAluno:

    def __init__(self):
        self.alunos = [
            # Aluno(1, 'Dudei', 'dudu@samurai.io', '(99) 123-123', 'dcc-01', ['bacharel','phd']),
            # Aluno(43, 'Thuzax', 'Thuzax@samurai.io', '(99) 433-334', 'dcc-43', ['bacharel','phd']),
        ]

    def add_aluno_p(self, p):
        l = [ x for x in self.alunos if x.idx == p.idx ]
        if len(l) > 0:
            return False
        
        self.alunos.append(p)

        return p.idx

    def get_alunos(self):
        return self.alunos

    def get_aluno(self, idx):
        p = [ x for x in self.alunos if x.idx ==  idx ]
        if len(p) < 1:
            return None

        return p[0]
    
    def add_aluno(self, data):
        p = Aluno.from_dict(data)

        l = [ x for x in self.alunos if x.idx == p.idx ]
        if len(l) > 0:
            return False
        
        self.alunos.append(p)

        return p.idx

    def update_aluno(self, idx, data):
        l = [ x for x in self.alunos if x.idx == idx ]
        pprint(l)
        if len(l) < 1:
            return False

        p = l[0]
        p.set_from_dict(data)

        return True
    
    def delete_aluno(self, idx):
        self.alunos = [ x for x in self.alunos if x.idx != idx ]

        return True