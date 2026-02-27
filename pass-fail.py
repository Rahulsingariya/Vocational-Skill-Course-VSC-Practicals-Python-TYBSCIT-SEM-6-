m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
aggregate = total / 5

print("Total Marks =", total)
print("Aggregate =", aggregate)

if aggregate >= 75:
    print("Grade : Distinction")
elif aggregate >= 60:
    print("Grade : First Division")
elif aggregate >= 50:
    print("Grade : Second Division")
else:
    print("Grade : Fail")
