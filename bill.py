qty = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
discount = float(input("Enter discount (%): "))
tax = float(input("Enter tax (%): "))

total = qty * price
bill = total - (total * discount / 100) + (total * tax / 100)

print("Final bill amount =", bill)

