from Classes.studentClass import  *
from Classes.disciplineClass import *
from Classes.gradeClass import *
from Controller.Undo import *

def Menu():
    print("Menu:")
    print("1. Add ")
    print("2. Remove ")
    print("3. Update ")
    print("4. List")
    print("5. Search")
    print("6. Statistics")
    print("7. Undo")
    print("8. Redo\n")

def Menu2():
    print("1. Student")
    print("2. Discipline")
    print("3. Grade\n")
    print("Command:")

def Menu3():
    print("1. Student")
    print("2. Discipline\n")
    print("Command:")

def Menu4():
    print("1. ID")
    print("2. Name")

def Menu5():
    print("1. All students enrolled at a given discipline")
    print("2. All students failing at one or more disciplines")
    print("3. Students with the best school situation, sorted in descending order of their aggregated average")
    print("4. All disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline.\n")

def adding(no, l_students, l_discipline, l_undo):
    if no == 1:
        try:
            id2 = int(input("Student id:"))
        except ValueError as ve:
            print("ID not good")
            return
        if l_students.checking_id(id2) == -1:
            return
        name = input("Student Name:")
        l_students.add(Student(id2, name))
        l_undo.register_operation("adding", "student", id2, name)

    elif no == 2:
        try:
            id2 = int(input("Discipline id:"))
        except ValueError as ve:
            print("ID not good")
            return
        if l_discipline.checking_id(id2) == -1:
            return
        name = input("Discipline name:")
        l_discipline.add(Discipline(id2, name))
        l_undo.register_operation("adding", "discipline", id2, name)

def adding_gr(l_grade, l_students, l_discipline, l_undo):
    try:
        id4 = int(input("Gr: St id"))
        n4 = int(input("Gr: Dis id"))
        gr = int(input("Grade: "))
    except ValueError as ve:
        print("ID not good")
        return
    if l_students.checking_exist_id(n4) == 1 and l_discipline.checking_exist_id(id4) == 1 and gr <= 10 and gr >= 1:
        l_grade.add(Grade(n4, id4, gr))
        l_undo.register_operation("adding", "grade", id4, n4, gr)
    else:
        print("Grade not added")

def duplicate_out(l):
    s = []
    for i in l:
        if i not in s:
            s.append(i)
    return s
