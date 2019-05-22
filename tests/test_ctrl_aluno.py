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

        self.assertEqual(len(alunos), 1, 'Deve ter apenas um aluno')
        self.assertIsInstance(alunos[0], Aluno, 'Deveria conter um objeto da classe aluno')

    # def test__get_professor__professor(self):
    #     professor = self.ctrl.get_professor(1)
    #     self.assertAlmostEqual(professor, self.professores[0], 'Deveria retornar {}'.format(self.professores[0]))

    # def test__get_professor__none(self):
    #     professor = self.ctrl.get_professor(66)
    #     self.assertAlmostEqual(professor, None, 'Não deveria retornar um professor')
    
    # def test__add_professor_instanciado__professor(self):
    #     p = Professor(43, 'Thuzax', 'Thuzax@samurai.io', '(99) 433-334', 'dcc-43', ['bacharel','phd'])
    #     self.ctrl.add_professor_instanciado(p)

    #     p_ = self.ctrl.get_professor(43)
    #     self.assertEqual(p, p_, 'Deveria ser o mesmo objeto')

    # def test__update_professor__true(self):
    #     p = self.professores[0]
    #     p.nome = 'Ribolive'

    #     status = self.ctrl.update_professor(1, p.__dict__)
    #     self.assertTrue(status, 'Erro ao atualizar dado')
        
    #     p_ = self.ctrl.get_professor(1)
    #     self.assertEqual(p, p_, 'Deveria ser o mesmo objeto')

    # def test__update_professor__false(self):
    #     p = self.professores[0]
    #     p.nome = 'Ribolive'

    #     status = self.ctrl.update_professor(999, p.__dict__)
    #     self.assertFalse(status, 'Dado nao deveria existir')

    # def test__delete_professor__true(self):
    #     status = self.ctrl.delete_professor(1)
    #     self.assertTrue(status, 'Dado deveria existir')

    # def test__delete_professor__false(self):
    #     status = self.ctrl.delete_professor(5)
    #     self.assertFalse(status, 'Dado nao deveria existir')