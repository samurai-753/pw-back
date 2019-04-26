from model import Professor
from pprint import pprint

class CtrlProfessor:

    def __init__(self):
        self.professores = [
            #Professor(1, 'Dudei', 'dudu@samurai.io', '(99) 123-123', 'dcc-01', ['bacharel','phd']),
            #Professor(43, 'Thuzax', 'Thuzax@samurai.io', '(99) 433-334', 'dcc-43', ['bacharel','phd']),
        ]

    def get_professores(self):
        return self.professores

    def get_professor(self, idx):
        p = [ x for x in self.professores if x.idx ==  idx ]
        if len(p) < 1:
            return None

        return p[0]
    
    def add_professor_p(self, p):
        l = [ x for x in self.professores if x.idx == p.idx ]
        if len(l) > 0:
            return False
        
        self.professores.append(p)

        return p.idx

    def add_professor(self, data):
        p = Professor.from_dict(data)

        l = [ x for x in self.professores if x.idx == p.idx ]
        if len(l) > 0:
            return False
        
        self.professores.append(p)
        pprint(self.professores)

        return p.idx
    
    def update_professor(self, idx, data):
        l = [ x for x in self.professores if x.idx == idx ]
        pprint(l)
        if len(l) < 1:
            return False

        p = l[0]
        p.set_from_dict(data)

        return True
    
    def delete_professor(self, idx):
        self.professores = [ x for x in self.professores if x.idx != idx ]

        return True