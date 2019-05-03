from model import Professor
from dao import ProfessorDAO
from pprint import pprint

class CtrlProfessor:
    instancia = None
    
    class __CtrlProfessor:

        def get_professores(self):
            return ProfessorDAO().get_professores()

        def get_professor(self, idx):
            return ProfessorDAO().get_professor(idx)

        def add_professor_p(self, p):
            return ProfessorDAO().add_professor(p)

        def add_professor(self, data):
            p = Professor.from_dict(data)
            return ProfessorDAO().add_professor(p)
        
        def update_professor(self, idx, data):
            p = Professor.from_dict(data)
            p.idx = idx
            return ProfessorDAO().update_professor(p)
        
        def delete_professor(self, idx):
            return ProfessorDAO().delete_professor(idx)

    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__CtrlProfessor()

    def __getattr__(self, name):
        return getattr(self.instancia, name)