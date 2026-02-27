numbers = []
total = 0

num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    numbers.append(num)
    total = total + num
    num = int(input("Enter a number (-1 to stop): "))

print("Numbers entered:", numbers)
print("Sum of numbers =", total)
