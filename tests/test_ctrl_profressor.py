import unittest
from controller import CtrlProfessor
from model import Professor

class TestCtrlProfessor(unittest.TestCase):

    def setUp(self):
        self.ctrl = CtrlProfessor()
        self.professores = [
            Professor(1, 'Dudei', 'dudu@samurai.io', '(99) 123-123', 'dcc-01', ['bacharel','phd'])
        ]
        for p in self.professores:
            self.ctrl.add_professor_p(p)
    
    def test__get_professores__professores(self):
        professores = self.ctrl.get_professores()
        self.assertEqual(len(professores), 1, 'Deve ter apenas um professor')
        self.assertIsInstance(professores[0], Professor, 'Deve conter um objeto da classe Professor')

    def test__get_professor__professor(self):
        professor = self.ctrl.get_professor(1)
        self.assertAlmostEqual(professor, self.professores[0], 'Deveria retornar {}'.format(self.professores[0]))

    def test__get_professor__none(self):
        professor = self.ctrl.get_professor(66)
        self.assertAlmostEqual(professor, None, 'Não deveria retornar um professor')
    
    def test__add_professor_p__professor(self):
        p = Professor(43, 'Thuzax', 'Thuzax@samurai.io', '(99) 433-334', 'dcc-43', ['bacharel','phd'])
        self.ctrl.add_professor_p(p)

        p_ = self.ctrl.get_professor(43)
        self.assertEqual(p, p_, 'Deveria ser o mesmo objeto')

    def test__update_professor__true(self):
        p = self.professores[0]
        p.nome = 'Ribolive'

        status = self.ctrl.update_professor(1, p.__dict__)
        self.assertTrue(status, 'Erro ao atualizar dado')
        
        p_ = self.ctrl.get_professor(1)
        self.assertEqual(p, p_, 'Deveria ser o mesmo objeto')

    def test__update_professor__false(self):
        p = self.professores[0]
        p.nome = 'Ribolive'

        status = self.ctrl.update_professor(999, p.__dict__)
        self.assertFalse(status, 'Dado nao deveria existir')

    def test__delete_professor__true(self):
        status = self.ctrl.delete_professor(1)
        self.assertTrue(status, 'Dado deveria existir')

    def test__delete_professor__false(self):
        status = self.ctrl.delete_professor(5)
        self.assertFalse(status, 'Dado nao deveria existir')