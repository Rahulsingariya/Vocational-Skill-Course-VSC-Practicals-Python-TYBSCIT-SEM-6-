a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Largest number =", max(a, b))

num = int(input("Enter a number: "))
print("Number is Even" if num & 1 == 0 else "Number is Odd")

ch = input("Enter a character: ")
if ch.isalpha():
    print("Swapped case =", ch.swapcase())
else:
    print("Not an alphabet")

year = int(input("Enter year: "))
print("Leap Year" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Not a Leap Year")
