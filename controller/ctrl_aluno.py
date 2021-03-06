import random
from app import db
from model import Aluno, Pessoa
from schema import SchemaAluno
from sqlalchemy.exc import IntegrityError
from exception import ExceptionAlunoNaoEncontrado
from .ctrl_pessoa import CtrlPessoa


class CtrlAluno:    

    def __init__(self):
        self.schema_aluno = SchemaAluno(strict=True)
        self.schema_alunos = SchemaAluno(strict=True, many=True)
        self.ctrl_pessoa = CtrlPessoa()

    def add_aluno(self, data):    
        try:
            p = Pessoa(
                data['nome'], data['email'], data['telefone']
            )
            pessoa = self.ctrl_pessoa.add_pessoa(p)

            aluno = Aluno(pessoa['idx'])
            aluno.resumo = data.get('resumo')
            aluno.idx = random.randint(0x0000, 0xffff)
            db.session.add(aluno)
            db.session.commit()

            return self.dump_aluno(aluno)

        except IntegrityError as e:
            db.session.rollback()
            
            raise e
    
    def get_alunos(self):
        alunos = Aluno.query.order_by(Aluno.idx).all()

        return self.dump_alunos(alunos)

    def get_aluno(self, idx, dump=True):
        aluno = Aluno.query.get(idx)

        if dump:
            return self.dump_aluno(aluno)
        else:
            return aluno
    
    def delete_aluno(self, idx):
        aluno = Aluno.query.get(idx)
        self.ctrl_pessoa.delete_pessoa(aluno.detalhes_idx)

        db.session.delete(aluno)
        db.session.commit()
    
    def update_aluno(self, idx, nome, email, telefone, resumo):
        aluno = Aluno.query.get(idx)
        if not aluno:
            raise ExceptionAlunoNaoEncontrado('idx', idx)

        if nome:
            aluno.detalhes.nome = nome
        
        if email:
            aluno.detalhes.email = email
        
        if telefone:
            aluno.detalhes.telefone = telefone
        
        if resumo:
            aluno.resumo = resumo

        db.session.commit()

        return self.dump_aluno(aluno)

    def dump_aluno(self, aluno):
        return self.schema_aluno.dump(aluno).data
    
    def dump_alunos(self, alunos):
        return self.schema_alunos.dump(alunos).data