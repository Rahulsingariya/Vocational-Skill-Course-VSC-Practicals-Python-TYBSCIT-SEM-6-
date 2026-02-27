m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))

for i in range(m, n + 1):
    if i % 2 == 0:
        print(i, "- Even")
    else:
        print(i, "- Odd")
