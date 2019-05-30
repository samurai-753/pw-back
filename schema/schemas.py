from app import ma
from model import Pessoa, Aluno, Professor


class SchemaPessoa(ma.ModelSchema):
    class Meta:
        model = Pessoa


class SchemaProfessor(ma.ModelSchema):
    class Meta:
        model = Professor


class SchemaAluno(ma.ModelSchema):
    class Meta:
        model = Aluno