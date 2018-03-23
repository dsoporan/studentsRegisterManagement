from Classes.gradeClass import *
from Controller.Redo import *

class UndoOperation(object):
    def __init__(self, method, type, *args):
        self.method = method
        self.type = type
        self.args = args

    def get_method(self):
        return self.method

    def get_type(self):
        return self.type

    def get_args(self):
        return self.args

class UndoList(object):
    def __init__(self):
        self.list_undo = []

    def operations(self):
        return self.list_undo

    def printing(self):
        for u in self.list_undo:
            print(str(u))

    def register_operation(self, method, type,*args):
        self.list_undo.append(UndoOperation(method, type,*args))

class UndoController(object):
    def __init__(self, l_undo, l_students, l_discipline, l_grade, l_redo):
        self.l_undo = l_undo
        self.l_students = l_students
        self.l_discipline = l_discipline
        self.l_grade = l_grade
        self.l_redo = l_redo

    def undo_add_student(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "adding":
                if l_undo_all[leng].get_type() == "student":
                    self.l_redo.register_operation("adding", "student", self.l_students.find_student(l_undo_all[leng].get_args()[0]))
                    self.l_students.removing(self.l_students.find_student(l_undo_all[leng].get_args()[0]))


    def undo_add_discipline(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "adding":
                if l_undo_all[leng].get_type() == "discipline":
                    self.l_redo.register_operation("adding", "discipline", self.l_discipline.find_discipline(l_undo_all[leng].get_args()[0]))
                    self.l_discipline.removing(self.l_discipline.find_discipline(l_undo_all[leng].get_args()[0]))


    def undo_add_grade(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "adding":
                if l_undo_all[leng].get_type() == "grade":
                    self.l_redo.register_operation("adding", "grade", Grade(l_undo_all[leng].get_args()[1], l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[2]))
                    self.l_grade.removing(Grade(l_undo_all[leng].get_args()[1], l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[2]))

    def undo_remove_student(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "removing":
                if l_undo_all[leng].get_type() == "student":
                    self.l_redo.register_operation("removing", "student", l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[1])
                    self.l_students.add(Student(l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[1]))


    def undo_remove_discipline(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "removing":
                if l_undo_all[leng].get_type() == "discipline":
                    self.l_redo.register_operation("removing", "discipline", Discipline(l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[1]))
                    self.l_discipline.add(Discipline(l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[1]))


    def undo_update_student(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "updating":
                if l_undo_all[leng].get_type() == "student":
                    self.l_redo.register_operation("updating", "student", l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[2], l_undo_all[leng].get_args()[3])
                    self.l_students.updating(l_undo_all[leng].get_args()[2], l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[1])


    def undo_update_discipline(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng > -1:
            if l_undo_all[leng].get_method() == "updating":
                if l_undo_all[leng].get_type() == "discipline":
                    self.l_redo.register_operation("updating", "discipline", l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[2], l_undo_all[leng].get_args()[3])
                    self.l_discipline.updating(l_undo_all[leng].get_args()[2], l_undo_all[leng].get_args()[0], l_undo_all[leng].get_args()[1])


    def check_emptyness(self):
        l_undo_all = self.l_undo.operations()
        leng = len(l_undo_all) - 1
        if leng < 0:
            print("Undo NOT done. You cannot undo anymore")


