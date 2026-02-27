class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    pass

b = Bike()

choice = input("Start vehicle? (yes/no): ")

if choice.lower() == "yes":
    b.start()
