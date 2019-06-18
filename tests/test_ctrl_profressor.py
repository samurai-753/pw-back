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
    
    def get_professor(self, idx):
        res = self.app.get(
            '/api/professor/{}'.format(idx)
        )

        return json.loads(res.data.decode('utf-8'))

    def post_professor(self, professor):
        res = self.app.post(
            '/api/professor',
            data=json.dumps(professor),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))
    
    def patch_professor(self, idx, dados):
        res = self.app.patch(
            '/api/professor/{}'.format(idx),
            data=json.dumps(dados),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))

    def delete_professor(self, idx):
        res = self.app.delete(
            '/api/professor/{}'.format(idx)
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
    
    def test__post_professor__400(self):
        p = self.professores[1]
        p.pop('sala', None)
        data = self.post_professor(p)

        self.assertEqual(400, data['status'])
        self.assertEqual("KeyNotFound 'sala'", data['message'])
    
    def test__get_professores__vazio(self):
        res = self.app.get('/api/professor')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertFalse(data['data'])

    def test__get_professores__lista(self):
        for p in self.professores:
            self.post_professor(p)

        res = self.app.get('/api/professor')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(len(self.professores), len(data['data']))
    
    def test__get_professor_idx__404(self):
        data = self.get_professor(42)

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound 42', data['message'])
    
    def test__get_professor_idx__200(self):
        p = self.professores[0]
        d = self.post_professor(p)
        idx = d['data']['idx']

        data = self.get_professor(idx)

        self.assertEqual(200, data['status'])
        self.assert_professor_equal(data['data'], p)
    
    def test__update_professor_idx__404(self):
        data = self.patch_professor(42, {})    

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound 42', data['message'])
    
    def test__update_professor_idx__200(self):
        p = self.professores[0]
        d = self.post_professor(p)
        idx = d['data']['idx']

        mod = dict(nome='Jão Bara')
        p['nome'] = 'Jão Bara'
        data = self.patch_professor(idx, mod)

        self.assertEqual(200, data['status'])
        self.assert_professor_equal(data['data'], p)
    
    def test__delete_professor_idx__404(self):
        data = self.delete_professor(42)    

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound 42', data['message'])
    
    def test__delete_professor_idx__200(self):
        p = self.professores[0]
        data = self.post_professor(p)
        self.assertEqual(200, data['status'])

        idx = data['data']['idx']
        
        data = self.delete_professor(idx)
        self.assertEqual(200, data['status'])

        data = self.get_professor(idx)

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound {}'.format(idx), data['message'])