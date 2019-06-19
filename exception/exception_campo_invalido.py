

class ExceptionCampoInvalido(Exception):
    def __init__(self, nome_classe, campo):
        self.nome_classe = nome_classe
        self.campo = campo

    def __str__(self):
        text = "Erro: " 
        text += str(self.nome_classe) + " não tem o campo " 
        text += "\"" + str(self.campo) + "\""
        text += "\n"
        return text


class ExceptionAlunoCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Aluno", campo)


class ExceptionBibTeXCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "BibTeX", campo)


class ExceptionDisciplinaCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Disciplina", campo)


class ExceptionDocumentoCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Documento", campo)


class ExceptionExtensaoCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Extensao", campo)


class ExceptionPessoaCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Pessoa", campo)


class ExceptionProfessorCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Professor", campo)


class ExceptionProjetoPesquisaCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "ProjetoPesquisa", campo)


class ExceptionPublicacaoCampoInvalido(ExceptionCampoInvalido):

    def __init__(self, campo):
        ExceptionCampoInvalido.__init__(self, "Publicacao", campo)


try:
    raise ExceptionPublicacaoCampoInvalido("balela")
except Exception as e:
    print(e)