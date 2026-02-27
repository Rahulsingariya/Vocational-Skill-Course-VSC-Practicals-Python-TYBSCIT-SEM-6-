str = input("Enter a string :")
s = len(str)
space = 0

for i in range(s):
    if str[i] == " ":
        space += 1
    else:
        space = 0


print("Spaces :", space)

