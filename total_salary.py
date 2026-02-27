salary = float(input("Enter employee salary: "))
gender = input("Enter gender (M/F): ")

bonus = 0

if gender == 'M' or gender == 'm':
    bonus = salary * 0.05
elif gender == 'F' or gender == 'f':
    bonus = salary * 0.10

if salary < 10000:
    bonus = bonus + salary * 0.02

total_salary = salary + bonus

print("Bonus amount =", bonus)
print("Total salary to be paid =", total_salary)
