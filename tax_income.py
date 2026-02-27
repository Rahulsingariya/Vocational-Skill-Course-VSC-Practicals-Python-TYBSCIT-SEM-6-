income = float(input("Enter taxable income: "))

if income < 180000:
    tax = 0
elif income <= 300000:
    tax = income * 0.10
elif income <= 500000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax amount =", tax)
