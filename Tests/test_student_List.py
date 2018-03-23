from unittest import TestCase
from Classes.studentClass import *


class TestStudent_List(TestCase):
    def setUp(self):
        self.l = Student_List()
        self.s = Student(1, "Ana")
        self.s1 = Student(2, "Bogdan")
    def test_add(self):
        self.l.add(self.s)
        self.assertEqual(self.l.get_all()[0].get_id(), 1)
        self.assertEqual(self.l.get_all()[0].get_name(), "Ana")

    def test_removee(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.l.removee(0)
        self.assertEqual(self.l.get_all()[0].get_id(), 2)
        self.assertEqual(self.l.get_all()[0].get_name(), "Bogdan")

    def test_removing(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.l.removing(self.s)
        self.assertEqual(self.l.get_all()[0].get_id(), 2)
        self.assertEqual(self.l.get_all()[0].get_name(), "Bogdan")

    def test_updating(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.l.updating(1, 11, "Avram")
        self.assertEqual(self.l.get_all()[0].get_id(), 11)
        self.assertEqual(self.l.get_all()[0].get_name(), "Avram")

    def test_checking_id(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.assertEqual(self.l.checking_id(1), -1)

    def test_checking_exist_id(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.assertEqual(self.l.checking_exist_id(1), 1)
        self.assertEqual(self.l.checking_exist_id(4), -1)

    def test_find_student(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.assertEqual(self.l.find_student(1).get_id(), 1)
        self.assertEqual(self.l.find_student(1).get_name(), "Ana")
        self.assertEqual(self.l.find_student(4), -1)

    def test_search_student(self):
        self.l.add(self.s)
        self.l.add(self.s1)
        self.assertEqual(self.l.search_student("a"), 1)
        self.assertEqual(self.l.search_student("bau"), -1)
