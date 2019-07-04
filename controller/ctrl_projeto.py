import random
import os
import hashlib
from pprint import pprint
from app import db
from model import Projeto
from schema import SchemaProjeto, SchemaProfessor
from controller import CtrlAluno, CtrlProfessor
from sqlalchemy.exc import IntegrityError
from exception import ExceptionProjetoNaoEncontrado, ExceptionProjetoCampoInvalido


class CtrlProjeto:
    
    def __init__(self):
        self.schema_projeto = SchemaProjeto(strict=True)
        self.schema_projetos = SchemaProjeto(strict=True, many=True)
        self.ctrl_aluno = CtrlAluno()
        self.ctrl_professor = CtrlProfessor()

    def add_projeto(self, data):
        try:
            projeto = Projeto(
                nome=data['nome'],
                orientador=self.ctrl_professor.get_professor(data['orientador'], dump=False),
                alunos=[ self.ctrl_aluno.get_aluno(a, dump=False) for a in data.get('alunos', []) ]
            )

            coorientador_idx = data.get('coorientador', None)
            if coorientador_idx:
                projeto.coorientador = self.ctrl_professor.get_professor(coorientador_idx , dump=False)

        except KeyError as e:
            raise ExceptionProjetoCampoInvalido(e)


        try:
            projeto.idx = random.randint(0x0000, 0xffff)
            db.session.add(projeto)
            db.session.commit()

            return self.dump_projeto(projeto)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )

    def get_projetos(self):
        projetos = Projeto.query.order_by(Projeto.idx).all()

        return self.dump_projetos(projetos)

    def get_projeto(self, idx):
        projeto = Projeto.query.get(idx)
        if not projeto:
            raise ExceptionProjetoNaoEncontrado('idx', idx)

        return self.dump_projeto(projeto)
    
    def delete_projeto(self, idx):
        projeto = Projeto.query.get(idx)
        if not projeto:
            raise ExceptionProjetoNaoEncontrado('idx', idx)

        db.session.delete(projeto)
        db.session.commit()
    
    def update_projeto(self, idx, data):
        projeto = Projeto.query.get(idx)
        if not projeto:
            raise ExceptionProjetoNaoEncontrado('idx', idx)

        if 'nome' in data:
            projeto.nome = data['nome']
        
        if 'orientador' in data:
            projeto.orientador = data['orientador']

        if 'coorientador' in data:
            projeto.coorientador = data['coorientador']

        if 'alunos' in data:
            projeto.alunos = data['alunos']

        db.session.commit()

        return self.dump_projeto(projeto)

    def dump_projeto(self, projeto):
        return self.schema_projeto.dump(projeto).data
    
    def dump_projetos(self, projetos):
        return self.schema_projetos.dump(projetos).data