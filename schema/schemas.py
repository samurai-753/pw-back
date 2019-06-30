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

class SchemaPublicacao(ma.ModelSchema):
    documento = ma.Nested(SchemaDocumento, exclude=('idx', ))

    class Mata:
        model = Publicacao

class SchemaExtensao(ma.ModelSchema):
    pessoa = ma.Nested(SchemaPessoa)
    publicacoes = ma.Nested(SchemaPublicacao)

    class Meta:
        model = Extensao