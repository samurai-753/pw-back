import unittest
import json
import datetime as dt
from io import BytesIO
from pprint import pprint
from app import app, db
from routes import app_disciplina, app_professor, app_documento, app_main
from model import Disciplina, User
from schema import SchemaDisciplina
from exception import ExceptionDisciplinaCampoInvalido, ExceptionDisciplinaNaoEncontrado


class TestDisciplina(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_disciplina)
        app.register_blueprint(app_professor)
        app.register_blueprint(app_documento)
        app.register_blueprint(app_main)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()
        self.get_token()

        self.schema_disciplina = SchemaDisciplina(strict=True)
        self.schema_disciplinas = SchemaDisciplina(strict=True, many=True)
        
        professores = [
            dict(nome='Gabriel Ribolive', email='ribolive@samurai.io', telefone='123', sala='dcc08'),
            dict(nome='Arthur Cruz', email='thuzax@samurai.io', telefone='123', sala='dcc47'),
            dict(nome='Breno Gomes', email='brenex@samurai.io', telefone='123', sala='dcc33'),
        ]
        
        prof_idx = []
        for p in professores:
            p_ = self.post_professor(p)
            prof_idx.append(p_['data']['idx'])

        documentos = [
            (BytesIO(b'e621'), 'e621.txt'),
            (BytesIO(b'boba'), 'boba.txt'),
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

        self.disciplinas = [
            dict(nome='ISBD', tipo='GRAD', professor=prof_idx[0], documentos=[docs_idx[0]]),
            dict(nome='ISBD', tipo='GRAD', professor=prof_idx[1], documentos=docs_idx)
        ]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        import os
        from app import UPLOAD_FOLDER
        for fl in os.listdir(UPLOAD_FOLDER):
            os.remove(os.path.join(UPLOAD_FOLDER, fl))
    
    def get_token(self):
        user = User('admin', 'admin')
        db.session.add(user)
        db.session.commit()

        res = self.app.post(
            '/login',
            data=json.dumps(dict(email='admin', password='admin')),
            content_type='application/json'
        )
        self.token = res.json['access_token']

    def post_professor(self, professor):
        res = self.app.post(
            '/api/professor',
            data=json.dumps(professor),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return res.json
    
    def get_disciplina(self, idx):
        res = self.app.get(
            '/api/disciplina/{}'.format(idx)
        )

        return res.json

    def post_disciplina(self, disciplina):
        res = self.app.post(
            '/api/disciplina',
            data=json.dumps(disciplina, default=str),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return res.json
    
    def patch_disciplina(self, idx, dados):
        res = self.app.patch(
            '/api/disciplina/{}'.format(idx),
            data=json.dumps(dados),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))

    def delete_disciplina(self, idx):
        res = self.app.delete(
            '/api/disciplina/{}'.format(idx),
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))
    
    def dump_disciplina(self, person):
        return self.schema_disciplina.dump(person).data
    
    def dump_disciplinas(self, people):
        return self.schema_disciplinas.dump(people).data

    def assert_disciplina_equal(self, recived_disciplina, sent_disciplina):
        self.assertEqual(recived_disciplina['tipo'], sent_disciplina['tipo'])
        self.assertEqual(recived_disciplina['nome'], sent_disciplina['nome'])
        self.assertEqual(recived_disciplina['professor'], sent_disciplina['professor'])
        self.assertEqual(recived_disciplina['documentos'], sent_disciplina['documentos'])
    
    def test__post_disciplina__200(self):
        p = self.disciplinas[0]
        data = self.post_disciplina(p)

        self.assertEqual(200, data['status'])
        self.assert_disciplina_equal(data['data'], p)
    
    def test__post_disciplina__400(self):
        p = self.disciplinas[0]
        p.pop('professor', None)
        data = self.post_disciplina(p)

        self.assertEqual(400, data['status'])

        e = ExceptionDisciplinaCampoInvalido('\'professor\'')
        self.assertEqual(str(e), data['message'])
    
    def test__get_disciplinas__vazio(self):
        res = self.app.get('/api/disciplina')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertFalse(data['data'])

    def test__get_disciplinas__lista(self):
        for p in self.disciplinas:
            self.post_disciplina(p)

        res = self.app.get('/api/disciplina')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(len(self.disciplinas), len(data['data']))
    
    def test__get_disciplina_idx__404(self):
        data = self.get_disciplina(42)

        self.assertEqual(404, data['status'])

        e = ExceptionDisciplinaNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__get_disciplina_idx__200(self):
        p = self.disciplinas[0]
        d = self.post_disciplina(p)
        idx = d['data']['idx']

        data = self.get_disciplina(idx)

        self.assertEqual(200, data['status'])
        self.assert_disciplina_equal(data['data'], p)
    
    def test__update_disciplina_idx__404(self):
        data = self.patch_disciplina(42, {})

        self.assertEqual(404, data['status'])
        e = ExceptionDisciplinaNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__update_disciplina_idx__200(self):
        p = self.disciplinas[0]
        d = self.post_disciplina(p)
        idx = d['data']['idx']

        mod = dict(nome='boba')
        p['nome'] = 'boba'
        data = self.patch_disciplina(idx, mod)

        self.assertEqual(200, data['status'])
        self.assert_disciplina_equal(data['data'], p)
    
    def test__delete_disciplina_idx__404(self):
        data = self.delete_disciplina(42)    

        self.assertEqual(404, data['status'])
        e = ExceptionDisciplinaNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__delete_disciplina_idx__200(self):
        p = self.disciplinas[0]
        data = self.post_disciplina(p)
        self.assertEqual(200, data['status'])

        idx = data['data']['idx']
        
        data = self.delete_disciplina(idx)
        self.assertEqual(200, data['status'])

        data = self.get_disciplina(idx)

        self.assertEqual(404, data['status'])
        e = ExceptionDisciplinaNaoEncontrado('idx', idx)
        self.assertEqual(str(e), data['message'])