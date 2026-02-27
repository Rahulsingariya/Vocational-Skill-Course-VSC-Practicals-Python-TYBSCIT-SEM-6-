class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def display(self):
        print("Name:", self.name)

name = input("Enter name: ")

s = Student(name)
s.display()
