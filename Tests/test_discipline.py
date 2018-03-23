from unittest import TestCase
from Classes.disciplineClass import *

class TestDiscipline(TestCase):
    def setUp(self):
        self.d = Discipline(1, "Mate")
    def test_get_id(self):
        self.assertEqual(self.d.get_id(), 1)

    def test_get_name(self):
        self.assertEqual(self.d.get_name(), "Mate")
