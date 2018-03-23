from Tools.tools import *

class StudentController(object):
    def __init__(self, l_students, l_grade):
        self.l_students = l_students
        # self.l_discipline = l_discipline
        self.l_grade = l_grade

    def removing_student(self, id2):
        student = self.l_students.find_student(id2)
        self.l_students.removing(student)
        while self.l_grade.find_grade2(id2) != -1:
            self.l_grade.removing(self.l_grade.find_grade2(student.get_id()))

    def best_students(self):
        l = self.l_grade.discipline_at_student()
        l = duplicate_out(l)
        l = sorted(l)
        i = 0
        while i < len(l):
            lsplit = l[i].split(" ")
            if lsplit[2] == "-1":
                l.remove(l[i])
                i -= 1
            i += 1
        i = 1
        lsplit = l[0].split(" ")
        st = lsplit[0]
        av = []
        av.append(float(lsplit[2]))
        new = []
        while i < len(l):
            lsplit = l[i].split(" ")
            if st == lsplit[0]:
                av.append(float(lsplit[2]))
            else:
                aver = sum(av) / float(len(av))
                new.append(str(aver) + " " + self.l_students.find_student(int(st)).get_name())
                st = lsplit[0]
                av = []
                av.append(float(lsplit[2]))
            if i == len(l) - 1:
                aver = sum(av) / float(len(av))
                new.append(str(aver) + " " + self.l_students.find_student(int(st)).get_name())
            i += 1
        new = sorted(new, reverse=True)
        i = 0
        while i < len(new):
            lsplit = new[i].split(" ")
            if lsplit[0] == "10.0":
                new.insert(0, new[i])
                new.pop(i + 1)
            i += 1
        print(new)