import random
import os
import hashlib
from app import db
from model import Disciplina
from schema import SchemaDisciplina
from sqlalchemy.exc import IntegrityError
from exception import ExceptionDisciplinaNaoEncontrado, ExceptionDisciplinaCampoInvalido
from .ctrl_documento import CtrlDocumento


class CtrlDisciplina:
    
    def __init__(self):
        self.schema_disciplina = SchemaDisciplina(strict=True)
        self.schema_disciplinas = SchemaDisciplina(strict=True, many=True)
        self.ctrl_documento = CtrlDocumento()

    def add_disciplina(self, data):
        try:
            disciplina = Disciplina(
                data['nome'], data['tipo'], data['professor']
            )
        except KeyError as e:
            raise ExceptionDisciplinaCampoInvalido(e)

        for d in data.get('documentos', []):
            doc = self.ctrl_documento.get_documento(d)
            disciplina.documentos.append(doc)

        try:
            disciplina.idx = random.randint(0x0000, 0xffff)
            db.session.add(disciplina)
            db.session.commit()

            return self.dump_disciplina(disciplina)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )

    def get_disciplinas(self):
        disciplinas = Disciplina.query.order_by(Disciplina.idx).all()

        return self.dump_disciplinas(disciplinas)

    def get_disciplina(self, idx):
        disciplina = Disciplina.query.get(idx)
        if not disciplina:
            raise ExceptionDisciplinaNaoEncontrado('idx', idx)

        return self.dump_disciplina(disciplina)
    
    def delete_disciplina(self, idx):
        disciplina = Disciplina.query.get(idx)
        if not disciplina:
            raise ExceptionDisciplinaNaoEncontrado('idx', idx)

        for doc in disciplina.documentos:
            db.session.delete(doc)

        db.session.delete(disciplina)
        db.session.commit()
    
    def update_disciplina(self, idx, data):
        disciplina = Disciplina.query.get(idx)
        if not disciplina:
            raise ExceptionDisciplinaNaoEncontrado('idx', idx)

        if 'nome' in data:
            disciplina.nome = data['nome']

        db.session.commit()

        return self.dump_disciplina(disciplina)

    def dump_disciplina(self, disciplina):
        return self.schema_disciplina.dump(disciplina).data
    
    def dump_disciplinas(self, disciplinas):
        return self.schema_disciplinas.dump(disciplinas).data