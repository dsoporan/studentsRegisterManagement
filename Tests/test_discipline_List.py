from unittest import TestCase
from Classes.disciplineClass import *

class TestDiscipline_List(TestCase):
    def setUp(self):
        self.l = Discipline_List()
        self.d = Discipline(1, "Mate")
        self.d1 = Discipline(2, "Info")

    def test_add(self):
        self.l.add(self.d)
        self.assertEqual(self.l.get_all()[0].get_id(), 1)
        self.assertEqual(self.l.get_all()[0].get_name(), "Mate")

    def test_removee(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.l.removee(0)
        self.assertEqual(self.l.get_all()[0].get_id(), 2)
        self.assertEqual(self.l.get_all()[0].get_name(), "Info")

    def test_removing(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.l.removing(self.d)
        self.assertEqual(self.l.get_all()[0].get_id(), 2)
        self.assertEqual(self.l.get_all()[0].get_name(), "Info")

    def test_updating(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.l.updating(1, 11, "Rom")
        self.assertEqual(self.l.get_all()[0].get_id(), 11)
        self.assertEqual(self.l.get_all()[0].get_name(), "Rom")

    def test_checking_id(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.assertEqual(self.l.checking_id(1), -1)

    def test_checking_exist_id(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.assertEqual(self.l.checking_exist_id(1), 1)
        self.assertEqual(self.l.checking_exist_id(44), -1)

    def test_find_discipline(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.assertEqual(self.l.find_discipline(1).get_id(), 1)
        self.assertEqual(self.l.find_discipline(1).get_name(), "Mate")
        self.assertEqual(self.l.find_discipline(4), -1)

    def test_find_by_name(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.assertEqual(self.l.find_by_name("Mate"), 1)
        self.assertEqual(self.l.find_by_name("MMM"), -1)

    def test_search_discipline(self):
        self.l.add(self.d)
        self.l.add(self.d1)
        self.assertEqual(self.l.search_discipline("m"), 1)
        self.assertEqual(self.l.search_discipline("bau"), -1)
