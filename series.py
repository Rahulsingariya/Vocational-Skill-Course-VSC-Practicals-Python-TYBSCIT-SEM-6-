x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))

power = x ** n
print("Power of x^n =", power)
sum1 = 0
for i in range(1, n + 1):
    sum1 = sum1 + (i / (i + 1))

print("Sum of series (i) =", sum1)
sum2 = 0
for i in range(1, n + 1):
    sum2 = sum2 + ((i * i) / i)

print("Sum of series (ii) =", sum2)
