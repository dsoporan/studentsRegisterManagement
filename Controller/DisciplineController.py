from Tools.tools import *

class DisciplineController(object):
    def __init__(self, l_discipline, l_grade):
        # self.l_students = l_students
        self.l_discipline = l_discipline
        self.l_grade = l_grade

    def removing_discipline(self, id2):
        discipline = self.l_discipline.find_discipline(id2)
        self.l_discipline.removing(discipline)
        while self.l_grade.find_grade(id2) != -1:
            self.l_grade.removing(self.l_grade.find_grade(discipline.get_id()))

    def disciplines_in_order(self):
        l = self.l_grade.student_at_discipline()
        l = duplicate_out(l)
        i = 1
        lsplit = l[0].split(" ")
        di = lsplit[0]
        av = []
        av.append(float(lsplit[2]))
        new = []
        while i < len(l):
            lsplit = l[i].split(" ")
            if di == lsplit[0]:
                av.append(float(lsplit[2]))
            else:
                aver = sum(av) / float(len(av))
                new.append(str(aver) + " " + self.l_discipline.find_discipline(int(di)).get_name())
                di = lsplit[0]
                av = []
                av.append(float(lsplit[2]))
            if i == len(l) - 1:
                aver = sum(av) / float(len(av))
                new.append(str(aver) + " " + self.l_discipline.find_discipline(int(di)).get_name())
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
