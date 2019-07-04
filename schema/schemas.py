from app import ma
from model import *


class SchemaPessoa(ma.ModelSchema):
    class Meta:
        model = Pessoa


class SchemaProfessor(ma.ModelSchema):
    detalhes = ma.Nested(SchemaPessoa, exclude=('idx', ))

    class Meta:
        model = Professor


class SchemaAluno(ma.ModelSchema):
    detalhes = ma.Nested(SchemaPessoa)

    class Meta:
        model = Aluno

class SchemaDocumento(ma.ModelSchema):
    class Meta:
        model = Documento
        exclude = ('path', )

class SchemaPublicacao(ma.ModelSchema):
    documento = ma.Nested(SchemaDocumento)

    class Meta:
        model = Publicacao

class SchemaExtensao(ma.ModelSchema):
    pessoa = ma.Nested(SchemaPessoa)
    publicacoes = ma.Nested(SchemaPublicacao)

    class Meta:
        model = Extensao

class SchemaDisciplina(ma.ModelSchema):
    # documentos = ma.Nested(SchemaDocumento)
    # professor = ma.Nested(SchemaProfessor)

    class Meta:
        model = Disciplina

class SchemaProjeto(ma.ModelSchema):
    # orientador = ma.Nested(SchemaProfessor)
    # coorientador = ma.Nested(SchemaProfessor)

    class Meta:
        model = Projeto
        