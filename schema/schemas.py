from app import ma
from model import Pessoa, Aluno, Professor


class SchemaPessoa(ma.ModelSchema):
    class Meta:
        model = Pessoa


class SchemaProfessor(ma.ModelSchema):
    detalhes = ma.Nested(SchemaPessoa)

    class Meta:
        model = Professor


class SchemaAluno(ma.ModelSchema):
    detalhes = ma.Nested(SchemaPessoa)

    class Meta:
        model = Aluno