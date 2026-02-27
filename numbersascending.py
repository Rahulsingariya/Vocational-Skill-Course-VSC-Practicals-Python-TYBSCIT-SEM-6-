n1 = int(input("Enter first number (n1): "))
n2 = int(input("Enter second number (n2): "))
if n1 > n2:
    n1, n2 = n2, n1

print("Even numbers in ascending order (inclusive):")

i = n1
while i <= n2:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

print("\nNumbers in descending order (exclusive):")

for i in range(n2 - 1, n1, -1):
    print(i, end=" ")
