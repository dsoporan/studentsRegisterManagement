from unittest import TestCase
from Classes.studentClass import *

class TestStudent(TestCase):
    def setUp(self):
        self.s = Student(1, "Ana")
    def test_get_id(self):
        self.assertEqual(self.s.get_id(), 1)

    def test_get_name(self):
        self.assertEqual(self.s.get_name(), "Ana")

    def test_set_id(self):
        self.s.set_id(2)
        self.assertEqual(self.s.get_id(), 2)

    def test_set_name(self):
        self.s.set_name("Mere")
        self.assertEqual(self.s.get_name(), "Mere")
