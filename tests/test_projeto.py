import unittest
import json
import datetime as dt
from io import BytesIO
from pprint import pprint
from app import app, db
from routes import app_projeto, app_professor, app_aluno, app_main
from model import Projeto, User
from schema import SchemaProjeto
from exception import ExceptionProjetoCampoInvalido, ExceptionProjetoNaoEncontrado


class TestProjeto(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.register_blueprint(app_main)
        app.register_blueprint(app_professor)
        app.register_blueprint(app_projeto)
        app.register_blueprint(app_aluno)


        db.create_all()
        self.get_token()

        self.schema_projeto = SchemaProjeto(strict=True)
        self.schema_projetos = SchemaProjeto(strict=True, many=True)
        
        professores = [
            dict(nome='Gabriel Ribolive', email='ribolive2@samurai.io', senha='a', telefone='123', sala='dcc08'),
            dict(nome='Arthur Cruz', email='thuzax2@samurai.io', senha='a', telefone='123', sala='dcc47'),
            dict(nome='Breno Gomes', email='brenex2@samurai.io', senha='a', telefone='123', sala='dcc33'),
        ]
        
        prof_idx = []
        for p in professores:
            p_ = self.post_professor(p)
            prof_idx.append(p_['data']['idx'])

        alunos = [
            dict(nome='Gabriel Ribolive', email='ribolive@samurai.io', telefone='123', resumo='Antigo carinha do CA'),
            dict(nome='Arthur Cruz', email='thuzax@samurai.io', telefone='123', resumo='Filho do Mayron'),
            dict(nome='Breno Gomes', email='brenex@samurai.io', telefone='123', resumo='???'),
        ]

        alunos_idx = []
        for a in alunos:
            a_ = self.post_aluno(a)
            alunos_idx.append(a_['data']['idx'])
        
        self.projetos = [
            dict(nome='LOOP', orientador=prof_idx[0], coorientador=prof_idx[1], alunos=alunos_idx),
            dict(nome='LabRI', orientador=prof_idx[2], alunos=[]),
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

    def post_professor(self, professor):
        res = self.app.post(
            '/api/professor',
            data=json.dumps(professor),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return res.json
    
    def post_aluno(self, aluno):
        res = self.app.post(
            '/api/aluno',
            data=json.dumps(aluno),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )
        return res.json
    
    def get_projeto(self, idx):
        res = self.app.get(
            '/api/projeto/{}'.format(idx)
        )

        return res.json

    def post_projeto(self, projeto):
        res = self.app.post(
            '/api/projeto',
            data=json.dumps(projeto, default=str),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return res.json
    
    def patch_projeto(self, idx, dados):
        res = self.app.patch(
            '/api/projeto/{}'.format(idx),
            data=json.dumps(dados),
            content_type='application/json',
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))

    def delete_projeto(self, idx):
        res = self.app.delete(
            '/api/projeto/{}'.format(idx),
            headers={ 'Authorization': self.token }
        )

        return json.loads(res.data.decode('utf-8'))
    
    def dump_projeto(self, person):
        return self.schema_projeto.dump(person).data
    
    def dump_projetos(self, people):
        return self.schema_projetos.dump(people).data

    def assert_projeto_equal(self, recived_projeto, sent_projeto):
        self.assertEqual(recived_projeto['nome'], sent_projeto['nome'])
        self.assertEqual(recived_projeto['orientador']['idx'], sent_projeto['orientador'])
        self.assertEqual(recived_projeto['coorientador']['idx'], sent_projeto['coorientador'])
        self.assertEqual(set(recived_projeto['alunos']), set(sent_projeto['alunos']))
    
    def test__post_projeto__200(self):
        p = self.projetos[0]
        data = self.post_projeto(p)


        self.assertEqual(200, data['status'])
        self.assertNotEquals(data['data'], {})
        self.assert_projeto_equal(data['data'], p)
    
    def test__post_projeto__400(self):
        p = self.projetos[0]
        p.pop('orientador', None)
        data = self.post_projeto(p)

        self.assertEqual(400, data['status'])

        e = ExceptionProjetoCampoInvalido('\'orientador\'')
        self.assertEqual(str(e), data['message'])
    
    def test__get_projetos__vazio(self):
        res = self.app.get('/api/projeto')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(data['data'], [])

    def test__get_projetos__lista(self):
        for p in self.projetos:
            res = self.post_projeto(p)

        res = self.app.get('/api/projeto')
        data = json.loads(res.data.decode('utf-8'))
        
        self.assertEqual(200, data['status'])
        self.assertEqual(len(self.projetos), len(data['data']))
    
    def test__get_projeto_idx__404(self):
        data = self.get_projeto(42)

        self.assertEqual(404, data['status'])

        e = ExceptionProjetoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__get_projeto_idx__200(self):
        p = self.projetos[0]
        d = self.post_projeto(p)
        idx = d['data']['idx']

        data = self.get_projeto(idx)

        self.assertEqual(200, data['status'])
        self.assert_projeto_equal(data['data'], p)
    
    def test__update_projeto_idx__404(self):
        data = self.patch_projeto(42, {})

        self.assertEqual(404, data['status'])
        e = ExceptionProjetoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__update_projeto_idx__200(self):
        p = self.projetos[0]
        d = self.post_projeto(p)
        idx = d['data']['idx']

        mod = dict(nome='boba')
        p['nome'] = 'boba'
        data = self.patch_projeto(idx, mod)

        self.assertEqual(200, data['status'])
        self.assert_projeto_equal(data['data'], p)
    
    def test__delete_projeto_idx__404(self):
        data = self.delete_projeto(42)    

        self.assertEqual(404, data['status'])
        e = ExceptionProjetoNaoEncontrado('idx', 42)
        self.assertEqual(str(e), data['message'])
    
    def test__delete_projeto_idx__200(self):
        p = self.projetos[0]
        data = self.post_projeto(p)
        self.assertEqual(200, data['status'])

        idx = data['data']['idx']
        
        data = self.delete_projeto(idx)
        self.assertEqual(200, data['status'])

        data = self.get_projeto(idx)

        self.assertEqual(404, data['status'])
        e = ExceptionProjetoNaoEncontrado('idx', idx)
        self.assertEqual(str(e), data['message'])