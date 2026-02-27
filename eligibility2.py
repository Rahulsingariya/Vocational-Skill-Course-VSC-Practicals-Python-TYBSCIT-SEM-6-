age = int(input("Enter age: "))

if age >= 18:
    print("Person is eligible to vote")
else:
    years_left = 18 - age
    print("Person is not eligible to vote")
    print("Years left to become eligible =", years_left)
