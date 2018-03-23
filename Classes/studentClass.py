class Student(object):
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    def __str__(self):
        return str(self.student_id) + " " + str(self.student_name)
    def get_id(self):
        """
        :return: The ID of the student
        """
        return   self.student_id
    def get_name(self):
        """
        :return: The name of the student
        """
        return self.student_name

    def set_id(self, id2):
        """
        Sets the id of the student, id2
        :param id2: the new id
        :return: None
        """
        self.student_id = id2
    def set_name(self, name):
        """
        Sets the name of the student, name
        :param name: the new name
        :return: None
        """
        self.student_name = name

class Student_List(object):
    def __init__(self):
        self.l_student = []

    def get_all(self):
        return self.l_student
    def add(self, student):
        """
        Adding an element to the student list
        :param student: A student with id and name
        :return: None
        """
        self.l_student.append(student)

    def removee(self, i):
        """
        Deletes one Student from the list of students
        :param i: the index of the Student
        :return: None
        """
        self.l_student.pop(i)

    def printing(self):
        """
        Printing the list of students
        :return:
        """
        for student in self.l_student:
            print(str(student))

    def removing(self, st):
        """
        Removes the student st
        :param st: A student type
        :return: None
        """
        for i, student in enumerate(self.l_student):
            if str(student) == str(st):
                self.removee(i)
                return

    def checking_id(self, id2):
        """
        Check if there exists an id in the list
        :param id2: id
        :return: -1 if exists
        """
        for student in self.l_student:
            if student.get_id() == id2:
                print("ID already in use")
                return -1
    def checking_exist_id(self, id2):
        """
        Check if there exists an id in the list
        :param id2: id
        :return: 1 if exists, -1 if not + printing
        """
        for student in self.l_student:
            if student.get_id() == id2:
                return 1
        return -1

    def updating(self, id2, new_id, new_name):
        """
        Updates a student with a new id and a new name
        :param id2: old id
        :param new_id: new id
        :param new_name: new name
        :return: None
        """
        for i, student in enumerate(self.l_student):
            if id2 == student.get_id():
                    self.l_student[i] = Student(new_id, new_name)

    def find_student(self, student_id):
        """
        Finding a student in a list
        :param student_id: id of the student
        :return: the Student if its found, -1 otherwise
        """
        for student in self.l_student:
            if student_id == student.get_id():
                return Student(student_id, student.get_name())
        return -1

    def search_student(self, name):
        ok = -1
        for student in self.l_student:
            if str(name.lower()) in str(student.get_name().lower()):
                print(student.__str__())
                ok = 1
        return ok

def students_init(l_student):
    """
    Initializing the list of students
    :param l_student: the list of students
    :return: none
    """
    l_student.add(Student(1, "Darian"))
    l_student.add(Student(2, "Dariusss"))
    l_student.add(Student(3, "Ana"))
    l_student.add(Student(4, "Alex"))
    l_student.add(Student(5, "Mere"))
    l_student.add(Student(6, "Salut"))
    l_student.add(Student(7, "Mirel"))
    l_student.add(Student(8, "Mara"))
    l_student.add(Student(9, "Anastasia"))
    l_student.add(Student(10, "Darian"))