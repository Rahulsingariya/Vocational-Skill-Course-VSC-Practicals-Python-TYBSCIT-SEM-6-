upper = 0
lower = 0
digit = 0
space = 0
alphabet = 0

ch = input("Enter a character (* to stop): ")

while ch != '*':
    if ch.isupper():
        upper = upper + 1
        alphabet = alphabet + 1
    elif ch.islower():
        lower = lower + 1
        alphabet = alphabet + 1
    elif ch.isdigit():
        digit = digit + 1
    elif ch == ' ':
        space = space + 1

    ch = input("Enter a character (* to stop): ")

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)
print("Digits =", digit)
print("Spaces =", space)
print("Alphabets =", alphabet)
