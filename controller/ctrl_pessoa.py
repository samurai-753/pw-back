import random
from app import db
from model import Pessoa
from schema import SchemaPessoa
from sqlalchemy.exc import IntegrityError


class CtrlPessoa:
    
    def __init__(self):
        self.schema_pessoa = SchemaPessoa(strict=True)
        self.schema_pessoas = SchemaPessoa(strict=True, many=True)

    def add_pessoa(self, pessoa):
        try:
            pessoa.idx = random.randint(0x0000, 0xffff)
            db.session.add(pessoa)
            db.session.commit()

            return self.dump_pessoa(pessoa)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )


    def dump_pessoa(self, pessoa):
        return self.schema_pessoa.dump(pessoa).data
    
    def dump_pessoas(self, pessoas):
        return self.schema_pessoas.dump(pessoas).data