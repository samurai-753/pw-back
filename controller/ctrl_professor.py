import random
from app import db
from model import Professor
from schema import SchemaProfessor
from sqlalchemy.exc import IntegrityError


class CtrlProfessor:
    
    def __init__(self):
        self.schema_professor = SchemaProfessor(strict=True)
        self.schema_professores = SchemaProfessor(strict=True, many=True)

    def add_professor(self, professor):
        try:
            professor.idx = random.randint(0x0000, 0xffff)
            db.session.add(professor)
            db.session.commit()

            return self.dump_professor(professor)

        except IntegrityError as e:
            db.session.rollback()
            
            return dict(
                error='IntegrityError',
                message=str(e)
            )


    def dump_professor(self, professor):
        return self.schema_professor.dump(professor).data
    
    def dump_professores(self, professores):
        return self.schema_professores.dump(professores).data