import unittest
from controller import CtrlAluno
from dao import AlunoDAO
from model import Aluno

class TestCtrlAluno(unittest.TestCase):

    def setUp(self):
        self.ctrl = CtrlAluno()
        self.alunos = [
            Aluno(2, 'ribolive', 'dudu@samurai.io', '(99) 123-7070', 'Menino pequeno'),
        ]
        for p in self.alunos:
            self.ctrl.add_aluno_instanciado(p)
    
    def test__get_alunos__alunos(self):
        AlunoDAO().db_fake = []
        alunos = self.ctrl.get_alunos()

        self.assertEqual(len(alunos), len(AlunoDAO().db_fake), 'Deve ter apenas um aluno')
        self.assertIsInstance(alunos[0], Aluno, 'Deveria conter um objeto da classe aluno')

    def test__get_aluno__aluno(self):
        aluno = self.ctrl.get_aluno(2)
        self.assertAlmostEqual(aluno, self.alunos[0], 'Deveria retornar {}'.format(self.alunos[0]))

    def test__get_professor__none(self):
        aluno = self.ctrl.get_aluno(66)
        self.assertAlmostEqual(aluno, None, 'Não deveria retornar um professor')
    
    def test__add_aluno_instanciado__aluno(self):
        a = Aluno(229, 'Thuzax', 'Thuzax@samurai.io', '(99) 433-334', 'Esse e do bao mas nao dos mió')
        self.ctrl.add_aluno_instanciado(a)

        a2 = self.ctrl.get_aluno(229)
        self.assertEqual(a, a2, 'Deveria ser o mesmo objeto')

    def test__update_aluno__true(self):
        a = self.alunos[0]
        a.nome = 'Ribombom'

        status = self.ctrl.update_aluno(2, a.__dict__)
        self.assertTrue(status, 'Erro ao atualizar dado')
        
        a2 = self.ctrl.get_aluno(2)
        self.assertEqual(a, a2, 'Deveria ser o mesmo objeto')

    def test__update_aluno__false(self):
        p = self.alunos[0]
        p.nome = 'Ribombom'

        status = self.ctrl.update_aluno(999, p.__dict__)
        self.assertFalse(status, 'Dado nao deveria existir')

    def test__delete_aluno__true(self):
        status = self.ctrl.delete_aluno(2)
        self.assertTrue(status, 'Dado deveria existir')

    def test__delete_aluno__false(self):
        status = self.ctrl.delete_aluno(5)
        self.assertFalse(status, 'Dado nao deveria existir')