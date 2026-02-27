class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student Name:", self.name)

name = input("Enter name: ")
s = Student(name)
s.show()
