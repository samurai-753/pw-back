import unittest
import json
import datetime as dt
from io import BytesIO
from pprint import pprint
from app import app, db
from routes import app_publicacao, app_documento, app_main
from model import Publicacao, User
from schema import SchemaPublicacao
from exception import ExceptionPublicacaoCampoInvalido, ExceptionPublicacaoNaoEncontrado


class TestPublicacao(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_publicacao)
        app.register_blueprint(app_documento)
        app.register_blueprint(app_main)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()
        self.get_token()

        self.schema_publicacao = SchemaPublicacao(strict=True)
        self.schema_publicacoes = SchemaPublicacao(strict=True, many=True)
        
        documentos = [
            (BytesIO(b'e621'), 'e621.txt'),
            (BytesIO(b'boba'), 'boba.txt'),
            (BytesIO(b'fa'), 'fa.png'),
        ]

        docs_idx = []
        for d in documentos:
            res = self.app.post(
                '/api/documento',
                 content_type='multipart/form-data',
                 data={'file': d},
                 headers={ 'Authorization': self.token }
            )
            docs_idx.append(res.json['data']['idx'])

        self.publicacoes = [
            dict(info='um teste', tipo='CON', documento=docs_idx[0]),
            dict(info='dois teste', tipo='CON', documento=docs_idx[0]),
            dict(info='três teste', tipo='CON', documento=docs_idx[0]),
        ]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        import os
        from app import UPLOAD_FOLDER
        for fl in os.listdir(UPLOAD_FOLDER):
            os.remove(os.path.join(UPLOAD_FOLDER, fl))
    
    def get_token(self):
        user = User('admin', 'admin', None)
        db.session.add(user)
        db.session.commit()

        res = self.app.post(
            '/api/login',
            data=json.dumps(dict(email='admin', password='admin')),
            content_type='application/json'
        )
        self.token = res.json['access_token']

    def dump_publicacao(self, person):
        return self.schema_publicacao.dump(person).data
    
    def dump_publicacoes(self, people):
        return self.schema_publicacoes.dump(people).data
    
    def get_publicacao(self, idx):
        res = self.app.get(
            '/api/publicacao/{}'.format(idx),
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))

    def post_publicacao(self, publicacao):
        res = self.app.post(
            '/api/publicacao',
            data=json.dumps(publicacao, default=str),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))
    
    def patch_publicacao(self, idx, dados):
        res = self.app.patch(
            '/api/publicacao/{}'.format(idx),
            data=json.dumps(dados),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))

    def delete_publicacao(self, idx):
        res = self.app.delete(
            '/api/publicacao/{}'.format(idx),
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))

    def assert_publicacao_equal(self, recived_publicacao, sent_publicacao):
        self.assertEqual(recived_publicacao['tipo'], sent_publicacao['tipo'])
        self.assertEqual(recived_publicacao['info'], sent_publicacao['info'])
        self.assertEqual(recived_publicacao['documento']['idx'], sent_publicacao['documento'])
    
    def test__post_publicacao__200(self):
        p = self.publicacoes[0]
        data = self.post_publicacao(p)

        self.assertEqual(200, data['status'])
        self.assert_publicacao_equal(data['data'], p)
    
    def test__post_publicacao__400(self):
        p = self.publicacoes[0]
        p.pop('info', None)
        data = self.post_publicacao(p)

        self.assertEqual(400, data['status'])

        e = ExceptionPublicacaoCampoInvalido('\'info\'')
        self.assertEqual(str(e), data['message'])
    
    def test__get_publicacoes__vazio(self):
        res = self.app.get('/api/publicacao')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertFalse(data['data'])

    def test__get_publicacoes__lista(self):
        for p in self.publicacoes:
            self.post_publicacao(p)

        res = self.app.get('/api/publicacao')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(len(self.publicacoes), len(data['data']))
    
    def test__get_publicacao_idx__404(self):
        data = self.get_publicacao(42)

        self.assertEqual(404, data['status'])

        e = ExceptionPublicacaoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__get_publicacao_idx__200(self):
        p = self.publicacoes[0]
        d = self.post_publicacao(p)
        idx = d['data']['idx']

        data = self.get_publicacao(idx)

        self.assertEqual(200, data['status'])
        self.assert_publicacao_equal(data['data'], p)
    
    def test__update_publicacao_idx__404(self):
        data = self.patch_publicacao(42, {})

        self.assertEqual(404, data['status'])
        e = ExceptionPublicacaoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__update_publicacao_idx__200(self):
        p = self.publicacoes[0]
        d = self.post_publicacao(p)
        idx = d['data']['idx']

        mod = dict(tipo='RES')
        p['tipo'] = 'RES'
        data = self.patch_publicacao(idx, mod)

        self.assertEqual(200, data['status'])
        self.assert_publicacao_equal(data['data'], p)
    
    def test__delete_publicacao_idx__404(self):
        data = self.delete_publicacao(42)    

        self.assertEqual(404, data['status'])
        e = ExceptionPublicacaoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__delete_publicacao_idx__200(self):
        p = self.publicacoes[0]
        data = self.post_publicacao(p)
        self.assertEqual(200, data['status'])

        idx = data['data']['idx']
        
        data = self.delete_publicacao(idx)
        self.assertEqual(200, data['status'])

        data = self.get_publicacao(idx)

        self.assertEqual(404, data['status'])
        e = ExceptionPublicacaoNaoEncontrado('idx', idx)
        self.assertEqual(str(e), data['message'])