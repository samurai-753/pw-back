class ExceptionNaoEncontrado(Exception):

    def __init__(self, nome_classe, campo, valor):
        self.nome_classe = nome_classe
        self.campo = campo
        self.valor = valor

    def __str__(self):
        text = "Erro: " 
        text += str(self.nome_classe) + " com " + str(self.campo) + "=" + str(self.valor) 
        text += " não encontrado\n"
        return text


class ExceptionAlunoNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Aluno", campo, valor)


class ExceptionBibTeXNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "BibTeX", campo, valor)


class ExceptionDisciplinaNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Disciplina", campo, valor)


class ExceptionDocumentoNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Documento", campo, valor)


class ExceptionExtensaoNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Extensao", campo, valor)


class ExceptionPessoaNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Pessoa", campo, valor)


class ExceptionProfessorNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Professor", campo, valor)


class ExceptionProjetoNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Projeto", 
                                        campo, valor)


class ExceptionPublicacaoNaoEncontrado(ExceptionNaoEncontrado):

    def __init__(self, campo, valor):
        ExceptionNaoEncontrado.__init__(self, "Publicacao", campo, valor)
