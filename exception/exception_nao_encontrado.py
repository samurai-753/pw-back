

class ExceptionPessoaNaoEncontrado(Exception):
    def __init__(self, idx=0):
        Exception.__init__(self)
        self.idx = idx
        
    def __str__(self):
        text = "Erro: pessoa com id=" + str(self.idx) + " não encontrado\n"
        return text

class ExceptionProfessorNaoEncontrado(ExceptionPessoaNaoEncontrado):
    def __str__(self):
        text = "Erro: professor com id=" + str(self.idx) + " não encontrado\n"
        return text


class ExceptionAlunoNaoEncontrado(ExceptionProfessorNaoEncontrado):
    def __str__(self):
        text = "Erro: aluno com id=" + str(self.idx) + " não encontrado\n"
        return text

try:
    raise ExceptionAlunoNaoEncontrado(10)
except Exception as e:
    print(e)

