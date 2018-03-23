from Tools.tools import *
from Classes.gradeClass import *

class GradeController(object):
    def __init__(self, l_students, l_discipline, l_grade):
        self.l_students = l_students
        self.l_discipline = l_discipline
        self.l_grade = l_grade

    def students_at_discipline_alpha(self, id2, name):
        l = self.l_grade.list_students_from_discipline(id2)
        l = duplicate_out(l)
        print(l)
        i = 0
        nm = []
        while i < len(l):
            st = self.l_students.find_student(l[i])
            if st != -1:
                name = st.get_name()
                nm.append(name)
            else:
                print("Student not found")
                break
            i += 1
        if nm != []:
            print("Students ordered alphabetically: ", sorted(nm))
        else:
            print("There are no students at ", name)

    def students_at_discipline_avg(self, id2, name):
        l = self.l_grade.list_students_from_discipline(id2)
        l = duplicate_out(l)
        print(l)
        i = 0
        av = []
        while i < len(l):
            st = self.l_students.find_student(l[i])
            if st != -1:
                av.append(str(self.l_grade.student_grades_average(id2, l[i])) + " - " + str(st.get_name()))
            else:
                print("Student not found")
                break
            i += 1
        if av != []:
            print("Students ordered by grades average:", sorted(av, reverse=True))
        else:
            print("There are no students at ", name)

    def students_failing(self):
        l = self.l_grade.student_at_discipline()
        l = duplicate_out(l)
        l = sorted(l)
        i = 0
        while i < len(l):
            lsplit = l[i].split(" ")
            if float(lsplit[2]) < 5:
                di = self.l_discipline.find_discipline(int(lsplit[0]))
                st = self.l_students.find_student(int(lsplit[1]))
                print(di.get_name(), ":", st.get_name())
            i += 1
        print("\n")

