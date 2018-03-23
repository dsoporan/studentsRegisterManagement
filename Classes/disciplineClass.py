class Discipline(object):
    def __init__(self, discipline_id, discipline_name):
        self.discipline_id = discipline_id
        self.discipline_name = discipline_name

    def __str__(self):
        return str(self.discipline_id) + " " + str(self.discipline_name)

    def get_id(self):
        """
        :return: the id of the discipline
        """
        return   self.discipline_id
    def get_name(self):
        """
        :return: the name of the discipline
        """
        return self.discipline_name

class Discipline_List(object):
    def __init__(self):
        self.l_discipline = []

    def get_all(self):
            return self.l_discipline

    def add(self, discipline):
        """
         Adding an element to the discipline list
        :param student: A discipline with id and name
        :return: None
        """
        self.l_discipline.append(discipline)

    def printing(self):
        """
        Printing the list of disciplines
        :return:
        """
        for discipline in self.l_discipline:
            print(str(discipline))

    def removee(self, poz):
        """
        Deletes one discipline from the list of disciplines
        :param i: the index of the discipline
        :return: None
        """
        self.l_discipline.pop(poz)

    def removing(self, di):
        """
        Removes the discipline di
        :param di: A discipline
        :return: None
        """
        for i, discipline in enumerate(self.l_discipline):
            if str(discipline) == str(di):
                self.removee(i)
                return
        print("ID not found")

    def updating(self, id2, new_id, new_name):
        """
        Updates a discipline with a new id and a new name
        :param id2: old id
        :param new_id: new id
        :param new_name: new name
        :return: None
        """
        for i, discipline in enumerate(self.l_discipline):
            if id2 == discipline.get_id():
                self.l_discipline[i] = Discipline(new_id, new_name)
                break

    def checking_id(self, id2):
        """
        Check if there exists an id in the list
        :param id2: id
        :return: -1 if exists
        """
        for discipline in self.l_discipline:
            if discipline.get_id() == id2:
                print("ID already in use")
                return -1

    def checking_exist_id(self, id2):
        """
        Check if there exists an id in the list
        :param id2: id
        :return: 1 if exists, -1 if not + printing
        """
        for discipline in self.l_discipline:
            if discipline.get_id() == id2:
                return 1
        return -1

    def find_discipline(self, discipline_id):
        """
        Finding a discipline in a list
        :param discipline_id_id: id of the student
        :return: the discipline if its found, -1 otherwise
        """
        for discipline in self.l_discipline:
            if discipline_id == discipline.get_id():
                return Discipline(discipline_id, discipline.get_name())
        return -1

    def find_by_name(self, name):
        for discipline in self.l_discipline:
            if discipline.get_name() == name:
                return discipline.get_id()
        return -1

    def search_discipline(self, name):
        ok = -1
        for discipline in self.l_discipline:
            if str(name.lower()) in str(discipline.get_name().lower()):
                print(discipline.__str__())
                ok = 1
        return ok

def discipline_init(l_discipline):
    """
    Initializing the list of discipline
    :param l_discipline: the list of disciplines
    :return: none
    """
    l_discipline.add(Discipline(1, "Mate"))
    l_discipline.add(Discipline(2, "Romana"))
    l_discipline.add(Discipline(3, "Engleza"))
    l_discipline.add(Discipline(4, "Informatica"))
    l_discipline.add(Discipline(5, "FP"))
    l_discipline.add(Discipline(6, "Algebra"))
    l_discipline.add(Discipline(7, "Analiza"))
    l_discipline.add(Discipline(8, "Arhitectura"))
    l_discipline.add(Discipline(9, "TIC"))
    l_discipline.add(Discipline(10, "Sport"))