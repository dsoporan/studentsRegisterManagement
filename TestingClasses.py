from Controller.ControllerClass import *
from Controller.DisciplineController import *
from Controller.GradeController import *
from Tools.tools import *
from Classes.studentClass import *
from Classes.disciplineClass import *
from Controller.Undo import *
from Controller.Redo import *

class Start(object):
    """
    The "ui" class
    """
    def __init__(self, l_students, l_discipline, l_grade, l_undo, l_redo):
        self.l_students = l_students
        self.l_discipline = l_discipline
        self.l_grade = l_grade
        self.l_undo = l_undo
        self.l_redo = l_redo
    def start(self):
        """
        the "main" function
        :return: none
        """
        students_init(l_students)
        discipline_init(l_discipline)
        grade_init(l_grade)
        student_cont = StudentController(l_students, l_grade)
        discipline_cont = DisciplineController(l_discipline, l_grade)
        grade_cont = GradeController(l_students, l_discipline, l_grade)
        while True:
            ok = 1
            Menu()
            try:
                n = int(input("Command:"))
            except ValueError as ve:
                print("Error:", ve)
                break
            if n == 1:
                Menu2()
                try:
                    n2 = int(input())
                except ValueError as ve:
                    print("Error:", ve)
                    break
                if n2 == 1:
                    adding(n2, l_students, l_discipline, l_undo)
                elif n2 == 2:
                    adding(n2, l_students, l_discipline, l_undo)
                elif n2 == 3:
                    adding_gr(l_grade, l_students, l_discipline, l_undo)
            elif n == 2:
                Menu3()
                try:
                    n = int(input())
                except ValueError as ve:
                    print("Error:", ve)
                    break
                if n == 1:
                    print("Remove Student ID:")
                    try:
                        id2 = int(input())
                    except ValueError as ve:
                        print("ID not good")
                        ok = -1
                    if ok == 1:
                        l_undo.register_operation("removing", "student", id2, l_students.find_student(id2).get_name())
                        student_cont.removing_student(id2)
                if n == 2:
                    print("Remove Discipline ID:")
                    try:
                        id2 = int(input())
                    except ValueError as ve:
                        print("ID not good")
                        ok = -1
                    if ok == 1:
                        l_undo.register_operation("removing", "discipline", id2, l_discipline.find_discipline(id2).get_name())
                        discipline_cont.removing_discipline(id2)

            elif n == 3:
                Menu3()
                try:
                    n2 = int(input())
                except ValueError as ve:
                    print("Error:", ve)
                    break
                if n2 == 1:
                    try:
                        id2 = int(input("Student ID to be updated: "))
                        new_id = int(input("New Student ID:"))
                    except ValueError as ve:
                        print("ID not good", ve)
                        ok = -1
                    if ok == 1 and l_students.checking_exist_id(id2) == 1:
                        new_name = input("New Student name:")
                        if l_students.checking_exist_id(new_id) == -1:
                            l_undo.register_operation("updating", "student", id2, l_students.find_student(id2).get_name(), new_id, new_name)
                            l_students.updating(id2, new_id, new_name)
                        else:
                            print("ID already in use")
                elif n2 == 2:
                    try:
                        id2 = int(input("Discipline ID to be updated: "))
                        new_id = int(input("New Discipline ID:"))
                    except ValueError as ve:
                        print("ID not good")
                        ok = -1
                    if ok == 1 and l_discipline.checking_exist_id(id2) == 1:
                        new_name = input("New Discipline name:")
                        if l_discipline.checking_exist_id(new_id) == -1:
                            l_undo.register_operation("updating", "discipline", id2, l_discipline.find_discipline(id2).get_name(), new_id, new_name)
                            l_discipline.updating(id2, new_id, new_name)
                        else:
                            print("ID already in use")
            elif n == 4:
                Menu2()
                try:
                    n2 = int(input())
                except ValueError as ve:
                    print("Error:", ve)
                    break
                if n2 == 1:
                    l_students.printing()
                elif n2 == 2:
                    l_discipline.printing()
                elif n2 == 3:
                    l_grade.printing()
            elif n == 5:
                Menu3()
                try:
                    n2 = int(input())
                except ValueError as ve:
                    print("Error:", ve)
                    break
                Menu4()
                try:
                    n3 = int(input())
                except ValueError as ve:
                    print("Error:", ve)
                    break
                if n3 == 2:
                    if n2 == 1:
                        name = input("Nume: ")
                        if l_students.search_student(name) != -1:
                            pass
                        else:
                            print("Student not found")
                    elif n2 == 2:
                        name = input("Nume: ")
                        if l_discipline.search_discipline(name) != -1:
                            pass
                        else:
                            print("Discipline not found")
                elif n3 == 1:
                    if n2 == 1:
                        try:
                            id2 = int(input("ID: "))
                        except ValueError as ve:
                            print("Invalid ID", ve)
                            break
                        if l_students.find_student(id2) != -1:
                            st = l_students.find_student(id2)
                            print(st.__str__())
                    if n2 == 2:
                        try:
                            id2 = int(input("ID: "))
                        except ValueError as ve:
                            print("Invalid ID", ve)
                            break
                        if l_discipline.find_discipline(id2) != -1:
                            di = l_discipline.find_discipline(id2)
                            print(di.__str__())

                else:
                    print("Command not found")
                    break
            elif n == 6:
                Menu5()
                try:
                    n2 = int(input("Statistics number:\n"))
                except ValueError as ve:
                    print("Invalid", ve)
                    break
                if n2 == 1:
                    name = input("Name of Discipline:")
                    id2 = l_discipline.find_by_name(name)
                    if id2 == -1:
                        print("Discipline doesn't exists")
                    else:
                        try:
                            n3 = int(input("1.Alphabetically\n2.Descending average grades\nOption:"))
                        except ValueError as ve:
                            print("Invalid", ve)
                            break
                        if n3 == 1:
                            grade_cont.students_at_discipline_alpha(id2, name)
                        elif n3 == 2:
                            grade_cont.students_at_discipline_avg(id2, name)
                if n2 == 2:
                    grade_cont.students_failing()
                if n2 == 3:
                    student_cont.best_students()
                if n2 == 4:
                    discipline_cont.disciplines_in_order()
            elif n == 7:
                l_undo_cont = UndoController(l_undo, l_students, l_discipline, l_grade, l_redo)
                for i, j in enumerate(l_undo.operations()):
                    print(l_undo.operations()[i].get_method())
                    print(l_undo.operations()[i].get_type())
                    print(l_undo.operations()[i].get_args())
                l_undo_cont.check_emptyness()
                l_undo_cont.undo_add_student()
                l_undo_cont.undo_add_discipline()
                l_undo_cont.undo_add_grade()
                l_undo_cont.undo_remove_student()
                l_undo_cont.undo_remove_discipline()
                l_undo_cont.undo_update_student()
                l_undo_cont.undo_update_discipline()
                if len(l_undo.operations()) > 0:
                    l_undo.operations().pop()

            elif n == 8:
                l_redo_cont = RedoController(l_undo, l_students, l_discipline, l_grade, l_redo)
                for i, j in enumerate(l_redo.operations()):
                    print(l_redo.operations()[i].get_method())
                    print(l_redo.operations()[i].get_type())
                    print(l_redo.operations()[i].get_args())
                l_redo_cont.check_emptyness()
                l_redo_cont.redo_add_student()
                l_redo_cont.redo_add_discipline()
                l_redo_cont.redo_add_grade()
                l_redo_cont.redo_remove_student()
                l_redo_cont.redo_remove_discipline()
                l_redo_cont.redo_update_student()
                l_redo_cont.redo_update_discipline()
                if len(l_redo.operations()) > 0:
                    l_redo.operations().pop()
            else:
                print("Exiting...")
                break

l_students = Student_List()
l_discipline = Discipline_List()
l_grade = Grade_List()
l_undo = UndoList()
l_redo = RedoList()
st = Start(l_students, l_discipline, l_grade, l_undo, l_redo)
st.start()