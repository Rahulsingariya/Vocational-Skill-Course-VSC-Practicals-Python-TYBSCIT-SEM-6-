class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

choice = input("Enter yes to make animal sound: ")

if choice.lower() == "yes":
    d.sound()

d.bark()
