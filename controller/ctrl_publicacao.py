import random
import os
import hashlib
from app import db, UPLOAD_FOLDER
from model import Publicacao
from schema import SchemaPublicacao
from sqlalchemy.exc import IntegrityError
from exception import ExceptionPublicacaoNaoEncontrado, ExceptionPublicacaoCampoInvalido
from .ctrl_documento import CtrlDocumento


class CtrlPublicacao:
    
    def __init__(self):
        self.schema_publicacao = SchemaPublicacao(strict=True)
        self.schema_publicacacoes = SchemaPublicacao(strict=True, many=True)
        self.ctrl_documento = CtrlDocumento()

    def add_publicacao(self, data):
        try:
            publicacao = Publicacao(
                data['info'], data['tipo'], data['documento']
            )
        except KeyError as e:
            raise ExceptionPublicacaoCampoInvalido(e)

        try:
            publicacao.idx = random.randint(0x0000, 0xffff)
            db.session.add(publicacao)
            db.session.commit()

            return self.dump_publicacao(publicacao)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )

    def get_publicacacoes(self):
        publicacacoes = Publicacao.query.order_by(Publicacao.idx).all()

        return self.dump_publicacacoes(publicacacoes)

    def get_publicacao(self, idx):
        publicacao = Publicacao.query.get(idx)

        return self.dump_publicacao(publicacao)
    
    def delete_publicacao(self, idx):
        publicacao = Publicacao.query.get(idx)
        if not publicacao:
            raise ExceptionPublicacaoNaoEncontrado('idx', idx)
            
        self.ctrl_documento.delete_documento(publicacao.documento_idx)

        db.session.delete(publicacao)
        db.session.commit()
    
    def update_publicacao(self, idx, data):
        publicacao = Publicacao.query.get(idx)
        if not publicacao:
            raise ExceptionPublicacaoNaoEncontrado('idx', idx)

        if 'info' in data:
            publicacao.info = data['info']
        
        if 'tipo' in data:
            publicacao.tipo = data['tipo']

        if 'documento' in data:
            publicacao.documento = data['documento']

        db.session.commit()

        return self.dump_publicacao(publicacao)

    def dump_publicacao(self, publicacao):
        return self.schema_publicacao.dump(publicacao).data
    
    def dump_publicacacoes(self, publicacacoes):
        return self.schema_publicacacoes.dump(publicacacoes).data