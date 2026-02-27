class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class")

choice = input("Enter parent or child: ")

if choice.lower() == "parent":
    obj = Parent()
else:
    obj = Child()

obj.show()
