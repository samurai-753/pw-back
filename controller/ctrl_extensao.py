import random
from app import db
from model import Extensao
from schema import SchemaExtensao
from sqlalchemy.exc import IntegrityError
from exception import ExceptionExtensaoNaoEncontrado, ExceptionExtensaoCampoInvalido


class CtrlExtensao:    

    def __init__(self):
        self.schema_extensao = SchemaExtensao(strict=True)
        self.schema_extensoes = SchemaExtensao(strict=True, many=True)

    def add_extensao(self, data):
        try:
            extensao = Extensao(
                data['tipo'], data['inicio'], data['fim'],
                int(data['pessoa'])
            )
        except KeyError as e:
            raise ExceptionExtensaoCampoInvalido(e)
        
        
        try:
            extensao.idx = random.randint(0x0000, 0xffff)

            db.session.add(extensao)
            db.session.commit()

            return self.dump_extensao(extensao)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )
    
    def get_extensoes(self):
        extensoes = Extensao.query.order_by(Extensao.idx).all()

        return self.dump_extensoes(extensoes)

    def get_extensao(self, idx):
        extensao = Extensao.query.get(idx)

        return self.dump_extensao(extensao)
    
    def delete_extensao(self, idx):
        extensao = Extensao.query.get(idx)
        if not extensao:
            raise ExceptionExtensaoNaoEncontrado('idx', idx)

        db.session.delete(extensao)
        db.session.commit()
    
    def update_extensao(self, idx, data):
        extensao = Extensao.query.get(idx)
        if not extensao:
            raise ExceptionExtensaoNaoEncontrado('idx', idx)
        

        if 'tipo' in data:
            extensao.tipo = data['tipo']

        if 'inicio' in data:
            extensao.inicio = data['inicio']

        if 'fim' in data:
            extensao.fim = data['fim']

        db.session.commit()

        return self.dump_extensao(extensao)

    def dump_extensao(self, extensao):
        return self.schema_extensao.dump(extensao).data
    
    def dump_extensoes(self, extensoes):
        return self.schema_extensoes.dump(extensoes).data