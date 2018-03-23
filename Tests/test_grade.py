from unittest import TestCase
from Classes.gradeClass import *

class TestGrade(TestCase):
    def setUp(self):
        self.g = Grade(1, 1, 10)
    def test_get_id(self):
        self.assertEqual(self.g.get_id(), (1, 1))

    def test_get_name(self):
        self.assertEqual(self.g.get_grade(), 10)
