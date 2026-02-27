prime = 0
composite = 0

num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            prime = prime + 1
        else:
            composite = composite + 1

    num = int(input("Enter a number (-1 to stop): "))

print("Prime numbers count =", prime)
print("Composite numbers count =", composite)
