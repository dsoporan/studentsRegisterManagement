class RedoOperation(object):
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

class RedoList(object):
    def __init__(self):
        self.list_redo = []

    def operations(self):
        return self.list_redo

    def printing(self):
        for u in self.list_redo:
            print(str(u))

    def register_operation(self, method, type,*args):
        self.list_redo.append(RedoOperation(method, type,*args))

class RedoController(object):
    def __init__(self, l_undo, l_students, l_discipline, l_grade, l_redo):
        self.l_undo = l_undo
        self.l_students = l_students
        self.l_discipline = l_discipline
        self.l_grade = l_grade
        self.l_redo = l_redo

    def redo_add_student(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "adding":
                if l_redo_all[leng].get_type() == "student":
                    self.l_students.add(l_redo_all[leng].get_args()[0])


    def redo_add_discipline(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "adding":
                if l_redo_all[leng].get_type() == "discipline":
                    self.l_discipline.add(l_redo_all[leng].get_args()[0])


    def redo_add_grade(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "adding":
                if l_redo_all[leng].get_type() == "grade":
                    self.l_grade.add(l_redo_all[leng].get_args()[0])


    def redo_remove_student(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "removing":
                if l_redo_all[leng].get_type() == "student":
                    self.l_students.removing(l_redo_all[leng].get_args()[0])


    def redo_remove_discipline(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "removing":
                if l_redo_all[leng].get_type() == "discipline":
                    self.l_discipline.removing(l_redo_all[leng].get_args()[0])


    def redo_update_student(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "updating":
                if l_redo_all[leng].get_type() == "student":
                    self.l_students.updating(l_redo_all[leng].get_args()[0], l_redo_all[leng].get_args()[1], l_redo_all[leng].get_args()[2])


    def redo_update_discipline(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng > -1:
            if l_redo_all[leng].get_method() == "updating":
                if l_redo_all[leng].get_type() == "discipline":
                    self.l_discipline.updating(l_redo_all[leng].get_args()[0], l_redo_all[leng].get_args()[1], l_redo_all[leng].get_args()[2])


    def check_emptyness(self):
        l_redo_all = self.l_redo.operations()
        leng = len(l_redo_all) - 1
        if leng < 0:
            print("Redo NOT done. You cannot redo anymore")