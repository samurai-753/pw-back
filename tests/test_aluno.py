import unittest
import json
from pprint import pprint
from app import app, db
from routes import app_aluno
from model import Pessoa, Aluno
from schema import SchemaPessoa, SchemaAluno


class TestAluno(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_aluno)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()

        self.schema_aluno = SchemaAluno(strict=True)
        self.schema_alunos = SchemaAluno(strict=True, many=True)
        
        self.alunos = [
            dict(nome='Gabriel Ribolive', email='ribolive@samurai.io', telefone='123', resumo='Antigo carinha do CA'),
            dict(nome='Arthur Cruz', email='thuzax@samurai.io', telefone='123', resumo='Filho do Mayron'),
            dict(nome='Breno Gomes', email='brenex@samurai.io', telefone='123', resumo='???'),
        ]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def dump_aluno(self, person):
        return self.schema_aluno.dump(person).data
    
    def dump_alunos(self, people):
        return self.schema_alunos.dump(people).data
    
    def get_aluno(self, idx):
        res = self.app.get(
            '/api/aluno/{}'.format(idx)
        )

        return json.loads(res.data.decode('utf-8'))

    def post_aluno(self, aluno):
        res = self.app.post(
            '/api/aluno',
            data=json.dumps(aluno),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))
    
    def patch_aluno(self, idx, dados):
        res = self.app.patch(
            '/api/aluno/{}'.format(idx),
            data=json.dumps(dados),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))

    def delete_aluno(self, idx):
        res = self.app.delete(
            '/api/aluno/{}'.format(idx)
        )

        return json.loads(res.data.decode('utf-8'))

    def assert_aluno_equal(self, recived_aluno, sent_aluno):
        self.assertEqual(recived_aluno['detalhes']['nome'], sent_aluno['nome'])
        self.assertEqual(recived_aluno['detalhes']['telefone'], sent_aluno['telefone'])
        self.assertEqual(recived_aluno['detalhes']['email'], sent_aluno['email'])
        self.assertEqual(recived_aluno['resumo'], sent_aluno['resumo'])
    
    def test__post_aluno__200(self):
        p = self.alunos[0]
        data = self.post_aluno(p)

        self.assertEqual(200, data['status'])
        self.assert_aluno_equal(data['data'], p)
    
    def test__post_aluno__400(self):
        p = self.alunos[1]
        p.pop('resumo', None)
        data = self.post_aluno(p)

        self.assertEqual(400, data['status'])
        self.assertEqual("KeyNotFound 'resumo'", data['message'])
    
    def test__get_alunos__vazio(self):
        res = self.app.get('/api/aluno')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertFalse(data['data'])

    def test__get_alunos__lista(self):
        for p in self.alunos:
            self.post_aluno(p)

        res = self.app.get('/api/aluno')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(len(self.alunos), len(data['data']))
    
    def test__get_aluno_idx__404(self):
        data = self.get_aluno(42)

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound 42', data['message'])
    
    def test__get_aluno_idx__200(self):
        p = self.alunos[0]
        d = self.post_aluno(p)
        idx = d['data']['idx']

        data = self.get_aluno(idx)

        self.assertEqual(200, data['status'])
        self.assert_aluno_equal(data['data'], p)
    
    def test__update_aluno_idx__404(self):
        data = self.patch_aluno(42, {})

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound 42', data['message'])
    
    def test__update_aluno_idx__200(self):
        p = self.alunos[0]
        d = self.post_aluno(p)
        idx = d['data']['idx']

        mod = dict(nome='Jão Bara')
        p['nome'] = 'Jão Bara'
        data = self.patch_aluno(idx, mod)

        self.assertEqual(200, data['status'])
        self.assert_aluno_equal(data['data'], p)
    
    def test__delete_aluno_idx__404(self):
        data = self.delete_aluno(42)    

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound 42', data['message'])
    
    def test__delete_aluno_idx__200(self):
        p = self.alunos[0]
        data = self.post_aluno(p)
        self.assertEqual(200, data['status'])

        idx = data['data']['idx']
        
        data = self.delete_aluno(idx)
        self.assertEqual(200, data['status'])

        data = self.get_aluno(idx)

        self.assertEqual(404, data['status'])
        self.assertEqual('IdNotFound {}'.format(idx), data['message'])