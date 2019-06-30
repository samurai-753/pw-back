import unittest
import json
import datetime as dt
from pprint import pprint
from app import app, db
from routes import app_extensao
from model import Extensao
from schema import SchemaExtensao
from exception import ExceptionExtensaoCampoInvalido, ExceptionExtensaoNaoEncontrado


class TestExtensao(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_extensao)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()

        self.schema_extensao = SchemaExtensao(strict=True)
        self.schema_extensoes = SchemaExtensao(strict=True, many=True)
        
        self.extensoes = [
            dict(
                tipo=0, inicio=dt.date(2018, 3, 1).isoformat(),
                fim=dt.date(2019, 2, 25).isoformat(), pessoa=33,
                publicacoes=[1, 2, 3, 4]
            )
        ]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def dump_extensao(self, person):
        return self.schema_extensao.dump(person).data
    
    def dump_extensoes(self, people):
        return self.schema_extensoes.dump(people).data
    
    def get_extensao(self, idx):
        res = self.app.get(
            '/api/extensao/{}'.format(idx)
        )

        return json.loads(res.data.decode('utf-8'))

    def post_extensao(self, extensao):
        res = self.app.post(
            '/api/extensao',
            data=json.dumps(extensao, default=str),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))
    
    def patch_extensao(self, idx, dados):
        res = self.app.patch(
            '/api/extensao/{}'.format(idx),
            data=json.dumps(dados),
            content_type='application/json'
        )

        return json.loads(res.data.decode('utf-8'))

    def delete_extensao(self, idx):
        res = self.app.delete(
            '/api/extensao/{}'.format(idx)
        )

        return json.loads(res.data.decode('utf-8'))

    def assert_extensao_equal(self, recived_extensao, sent_extensao):
        self.assertEqual(recived_extensao['tipo'], sent_extensao['tipo'])
        self.assertEqual(recived_extensao['inicio'], sent_extensao['inicio'])
        self.assertEqual(recived_extensao['fim'], sent_extensao['fim'])
    
    def test__post_extensao__200(self):
        p = self.extensoes[0]
        data = self.post_extensao(p)

        self.assertEqual(200, data['status'])
        self.assert_extensao_equal(data['data'], p)
    
    def test__post_extensao__400(self):
        p = self.extensoes[0]
        p.pop('inicio', None)
        data = self.post_extensao(p)

        self.assertEqual(400, data['status'])

        e = ExceptionExtensaoCampoInvalido('\'inicio\'')
        self.assertEqual(str(e), data['message'])
    
    def test__get_extensoes__vazio(self):
        res = self.app.get('/api/extensao')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertFalse(data['data'])

    def test__get_extensoes__lista(self):
        for p in self.extensoes:
            self.post_extensao(p)

        res = self.app.get('/api/extensao')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(len(self.extensoes), len(data['data']))
    
    def test__get_extensao_idx__404(self):
        data = self.get_extensao(42)

        self.assertEqual(404, data['status'])

        e = ExceptionExtensaoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__get_extensao_idx__200(self):
        p = self.extensoes[0]
        d = self.post_extensao(p)
        idx = d['data']['idx']

        data = self.get_extensao(idx)

        self.assertEqual(200, data['status'])
        self.assert_extensao_equal(data['data'], p)
    
    def test__update_extensao_idx__404(self):
        data = self.patch_extensao(42, {})

        self.assertEqual(404, data['status'])
        e = ExceptionExtensaoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__update_extensao_idx__200(self):
        p = self.extensoes[0]
        d = self.post_extensao(p)
        idx = d['data']['idx']

        mod = dict(tipo=2)
        p['tipo'] = 2
        data = self.patch_extensao(idx, mod)

        self.assertEqual(200, data['status'])
        self.assert_extensao_equal(data['data'], p)
    
    def test__delete_extensao_idx__404(self):
        data = self.delete_extensao(42)    

        self.assertEqual(404, data['status'])
        e = ExceptionExtensaoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__delete_extensao_idx__200(self):
        p = self.extensoes[0]
        data = self.post_extensao(p)
        self.assertEqual(200, data['status'])

        idx = data['data']['idx']
        
        data = self.delete_extensao(idx)
        self.assertEqual(200, data['status'])

        data = self.get_extensao(idx)

        self.assertEqual(404, data['status'])
        e = ExceptionExtensaoNaoEncontrado('idx', idx)
        self.assertEqual(str(e), data['message'])