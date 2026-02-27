numbers = []
positive = 0
negative = 0

num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    numbers.append(num)

    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1

    num = int(input("Enter a number (-1 to stop): "))

print("Numbers entered:", numbers)
print("Positive numbers count =", positive)
print("Negative numbers count =", negative)
