n = int(input("Enter value of n: "))

sum1 = 0
for i in range(1, n + 1):
    sum1 = sum1 + (1 / i)

print("Sum of series (i) =", sum1)

sum2 = 0
for i in range(1, n + 1):
    sum2 = sum2 + (1 / (i * i))

print("Sum of series (ii) =", sum2)
