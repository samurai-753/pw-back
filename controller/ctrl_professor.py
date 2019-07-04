import random
from app import db
from model import Professor, Pessoa, User
from schema import SchemaProfessor
from sqlalchemy.exc import IntegrityError
from .ctrl_pessoa import CtrlPessoa


class CtrlProfessor:
    
    def __init__(self):
        self.schema_professor = SchemaProfessor(strict=True)
        self.schema_professores = SchemaProfessor(strict=True, many=True)
        self.ctrl_pessoa = CtrlPessoa()

    def add_professor(self, nome, email, senha, telefone, sala):
        pessoa = Pessoa(nome, email, telefone)
        pessoa_dict = self.ctrl_pessoa.add_pessoa(pessoa)

        professor = Professor(pessoa_dict['idx'], sala)

        try:
            professor.idx = random.randint(0x0000, 0xffff)
            user = User(email, senha, professor.idx)
            db.session.add(professor)
            db.session.add(user)
            db.session.commit()

            return self.dump_professor(professor)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )

    def get_professores(self):
        professores = Professor.query.order_by(Professor.idx).all()

        return self.dump_professores(professores)

    def get_professor(self, idx, dump=True):
        professor = Professor.query.get(idx)

        if dump:
            return self.dump_professor(professor)
        else:
            return professor
    
    def delete_professor(self, idx):
        professor = Professor.query.get(idx)
        if not professor:
            raise Exception('idx')
            
        self.ctrl_pessoa.delete_pessoa(professor.detalhes_idx)

        db.session.delete(professor)
        db.session.commit()
    
    def update_professor(self, idx, nome, email, telefone, sala):
        professor = Professor.query.get(idx)
        if not professor:
            raise Exception('idx')

        if nome:
            professor.detalhes.nome = nome
        
        if email:
            professor.detalhes.email = email
        
        if telefone:
            professor.detalhes.telefone = telefone
        
        if sala:
            professor.sala = sala

        db.session.commit()

        return self.dump_professor(professor)

    def dump_professor(self, professor):
        return self.schema_professor.dump(professor).data
    
    def dump_professores(self, professores):
        return self.schema_professores.dump(professores).data