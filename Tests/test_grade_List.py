from unittest import TestCase
from Classes.gradeClass import *

class TestGrade_List(TestCase):
    def setUp(self):
        self.l = Grade_List()
        self.g = Grade(1, 1, 10)
        self.g1 = Grade(2, 2, 4)

    def test_add(self):
        self.l.add(self.g)
        self.assertEqual(self.l.get_all()[0].get_id(), (1, 1))
        self.assertEqual(self.l.get_all()[0].get_grade(), 10)

    def test_removee(self):
        self.l.add(self.g)
        self.l.add(self.g1)
        self.l.removee(0)
        self.assertEqual(self.l.get_all()[0].get_id(), (2, 2))
        self.assertEqual(self.l.get_all()[0].get_grade(), 4)

    def test_removing(self):
        self.l.add(self.g)
        self.l.add(self.g1)
        self.l.removing(self.g)
        self.assertEqual(self.l.get_all()[0].get_id(), (2, 2))
        self.assertEqual(self.l.get_all()[0].get_grade(), 4)

    def test_checking_exist_id(self):
        self.l.add(self.g)
        self.l.add(self.g1)
        self.assertEqual(self.l.checking_exist_id(1,1), 1)
        self.assertEqual(self.l.checking_exist_id(1, 2), -1)

    def test_find_grade(self):
        self.l.add(Grade(1, 2, 9))
        self.assertEqual(self.l.find_grade(1).get_id(), (1, 2))
        self.assertEqual(self.l.find_grade(1).get_grade(), 9)
        self.assertEqual(self.l.find_grade(4), -1)

    def test_find_grade2(self):
        self.l.add(Grade(1, 2, 9))
        self.assertEqual(self.l.find_grade2(2).get_id(), (1, 2))
        self.assertEqual(self.l.find_grade2(2).get_grade(), 9)
        self.assertEqual(self.l.find_grade2(4), -1)

    def test_list_students_from_discipline(self):
        self.l.add(self.g)
        self.l.add(self.g1)
        l2 = self.l.list_students_from_discipline(2)
        self.assertEqual(l2[0], 2)

    def test_list_dis_from_stud(self):
        self.l.add(self.g)
        self.l.add(self.g1)
        l2 = self.l.list_dis_from_stud(1)
        self.assertEqual(l2[0], 1)

    def test_student_grades_average(self):
        self.l.add(self.g)
        self.assertEqual(self.l.student_grades_average(1,1), 10)

    def test_student_at_discipline(self):
        self.l.add(Grade(1, 2, 10))
        l2 = self.l.student_at_discipline()
        self.assertEqual(l2[0], ("1 2 10.0"))

    def test_discipline_at_student(self):
        self.l.add(Grade(1, 2, 10))
        l2 = self.l.discipline_at_student()
        self.assertEqual(l2[0], ("2 1 10.0"))
