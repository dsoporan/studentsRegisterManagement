from Tools.tools import *

class Grade(object):
    def __init__(self, di_id, st_id, grade):
        self.di_id = di_id
        self.st_id = st_id
        self.grade = grade
    def __str__(self):
        return str(self.di_id) + " " + str(self.st_id) + " " + str(self.grade)
    def get_id(self):
        """
        :return: the id of the student and the discipline
        """
        return self.di_id, self.st_id
    def get_grade(self):
        return self.grade

class Grade_List(object):
    def __init__(self):
        self.l_grade = []

    def get_all(self):
        return self.l_grade

    def add(self, grade):
        """
        adding a  grade in a list
        :param grade: the grade
        :return: none
        """
        self.l_grade.append(grade)

    def removee(self, poz):
        self.l_grade.pop(poz)

    def removing(self, gr):
        """
        Removes the grade gr
        :param gr: A grade
        :return: None
        """
        for i, grade in enumerate(self.l_grade):
            if str(grade) == str(gr):
                self.removee(i)
                return
        print("ID not found")

    def printing(self):
        for grade in self.l_grade:
            print(str(grade))

    def checking_exist_id(self, id2, id3):
        """
        checks if the student id and the discipline id exists
        :param id2: id of the student
        :param id3: id of the discipline
        :return: 1 if found, -1 + printing otherwise
        """
        for grade in self.l_grade:
            a, b = grade.get_id()
            print(a, b, id2, id3)
            if a == id2 and b == id3:
                return 1
        print("ID not found")
        return -1

    def find_grade(self, id2):
        """
        Finding a grade in a list
        :param id2: id of the discipline
        :return: the grade if its found, -1 otherwise
        """
        for grade in self.l_grade:
            a,b = grade.get_id()
            if id2 == a:
                c = grade.get_grade()
                return Grade(a, b, c)
        return -1

    def find_grade2(self, id2):
        """
        Finding a grade in a list
        :param id2: id of the student
        :return: the grade if its found, -1 otherwise
        """
        for grade in self.l_grade:
            a,b = grade.get_id()
            if id2 == b:
                c = grade.get_grade()
                return Grade(a, b, c)
        return -1

    def list_students_from_discipline(self, id2):
        l = []
        for grade in self.l_grade:
            a, b = grade.get_id()
            if a == id2:
                l.append(b)
        return l

    def list_dis_from_stud(self, id2):
        l = []
        for grade in self.l_grade:
            a, b = grade.get_id()
            if b == id2:
                l.append(a)
        return l

    def student_grades_average(self, id1, id2):
        gr = []
        for grade in self.l_grade:
            a, b = grade.get_id()
            if b == id2 and id1 == a:
                gr.append(grade.get_grade())
        if len(gr) != 0:
             return sum(gr) / float(len(gr))
        else:
            return -1
    def student_at_discipline(self):
        new = []
        for grade in self.l_grade:
            a, b = grade.get_id()
            l = self.list_students_from_discipline(a)
            l = duplicate_out(l)
            i = 0
            while i < len(l):
                new.append(str(a) + " " + str(l[i]) + " " + str(self.student_grades_average(a, l[i])))
                i += 1
        return new

    def discipline_at_student(self):
        new = []
        for grade in self.l_grade:
            a, b = grade.get_id()
            l = self.list_dis_from_stud(b)
            l = duplicate_out(l)
            i = 0
            while i < len(l):
                new.append(str(b) + " " + str(l[i]) + " " + str(self.student_grades_average(l[i], b)))
                i += 1
        return new



def grade_init(l_grade):
    """
    Inintializing the list of grades
    :param l_grade: list
    :return: none
    """
    l_grade.add(Grade(1, 1, 10))
    l_grade.add(Grade(1, 5, 4))
    l_grade.add(Grade(2, 4, 5))
    l_grade.add(Grade(4, 4, 4))
    l_grade.add(Grade(3, 2, 10))
    l_grade.add(Grade(2, 2, 3))
    l_grade.add(Grade(1, 2, 9))
    l_grade.add(Grade(5, 1, 5))
    l_grade.add(Grade(4, 1, 2))
    l_grade.add(Grade(5, 2, 10))
    l_grade.add(Grade(1, 1, 4))
    l_grade.add(Grade(7, 9, 9))
    l_grade.add(Grade(8, 6, 9))
    l_grade.add(Grade(8, 7, 10))