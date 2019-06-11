import unittest
import json
from pprint import pprint
from app import app, db
from routes import app_professor
from model import Professor, Pessoa
from schema import SchemaPessoa, SchemaProfessor


class TestCtrlProfessor(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_professor)
        self.app = app.test_client()
        db.create_all()

        self.schema_professor = SchemaProfessor(strict=True)
        self.schema_professores = SchemaProfessor(strict=True, many=True)
        
        self.professores = [
            dict(nome='Gabriel Ribolive', email='ribolive@samurai.io', telefone='123', sala='dcc08'),
            dict(nome='Arthur Cruz', email='thuzax@samurai.io', telefone='123', sala='dcc47'),
            dict(nome='Breno Gomes', email='brenex@samurai.io', telefone='123', sala='dcc33'),
        ]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def dump_professor(self, person):
        return self.schema_professor.dump(person).data
    
    def dump_professores(self, people):
        return self.schema_professores.dump(people).data
    
    def post_professor(self, professor):
        res = self.app.post(
            '/api/professor',
            data=json.dumps(professor),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))

    def assert_professor_equal(self, recived_prof, sent_prof):
        self.assertEqual(recived_prof['detalhes']['nome'], sent_prof['nome'])
        self.assertEqual(recived_prof['detalhes']['telefone'], sent_prof['telefone'])
        self.assertEqual(recived_prof['detalhes']['email'], sent_prof['email'])
        self.assertEqual(recived_prof['sala'], sent_prof['sala'])
    
    def test__post_professor__200(self):
        p = self.professores[0]
        data = self.post_professor(p)

        self.assertEqual(200, data['status'])
        self.assert_professor_equal(data['data'], p)