principal = float(input("Enter initial investment amount: "))
rate = float(input("Enter rate of interest (%): "))
years = int(input("Enter number of years: "))

amount = principal * (1 + rate / 100) ** years

print("Investment value at the end of year =", amount)
