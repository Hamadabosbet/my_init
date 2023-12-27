class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)