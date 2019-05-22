from model import Aluno
from dao import AlunoDAO
from pprint import pprint

class CtrlAluno:

    instancia = None

    class __CtrlAluno:

        def __init__(self):
            self.alunos = [
                # Aluno(1, 'Dudei', 'dudu@samurai.io', '(99) 123-123', 'dcc-01', ['bacharel','phd']),
                # Aluno(43, 'Thuzax', 'Thuzax@samurai.io', '(99) 433-334', 'dcc-43', ['bacharel','phd']),
            ]

        def add_aluno_instanciado(self, a):
            return AlunoDAO().add_aluno(a)

        def get_alunos(self):
            return AlunoDAO().get_alunos()

        def get_aluno(self, idx):
            return AlunoDAO().get_aluno(idx)

        def add_aluno(self, data):
            a = Aluno.from_dict(data)
            return AlunoDAO().add_aluno(a)

        def update_aluno(self, idx, data):
            a = Aluno.from_dict(data)
            a.idx = idx
            return AlunoDAO().update_aluno(idx, data)
        
        def delete_aluno(self, idx):
            return AlunoDAO().delete_aluno(idx)
    
    def __init__(self):
        if(self.instancia == None):
            self.instancia = self.__CtrlAluno()

    def __getattr__(self, name):
        return getattr(self.instancia, name)