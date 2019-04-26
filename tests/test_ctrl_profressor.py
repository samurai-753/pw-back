import unittest
from controller import CtrlProfessor
from model import Professor

class TestCtrlProfessor(unittest.TestCase):

    def setUp(self):
        self.ctrl = CtrlProfessor()
        self.professores = [
            Professor(1, 'Dudei', 'dudu@samurai.io', '(99) 123-123', 'dcc-01', ['bacharel','phd'])
        ]
        self.ctrl.professores = self.professores
    
    def test__get_professores(self):
        professores = self.ctrl.get_professores()
        self.assertEqual(len(professores), 1, 'Deve ter apenas um professor')
        self.assertIsInstance(professores[0], Professor, 'Deve conter um objeto da classe Professor')

    def test__get_professor(self):
        professor = self.ctrl.get_professor(1)
        self.assertAlmostEqual(professor, self.professores[0])