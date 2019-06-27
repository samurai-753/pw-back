from app import ma
from model import Pessoa, Aluno, Professor, Documento, Publicacao


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