temp = float(input("Enter temperature: "))
unit = input("Enter unit (f for Fahrenheit, c for Celsius): ")

if unit == 'f' or unit == 'F':
    new_temp = (temp - 32) * 5 / 9
    print("Temperature in Celsius =", new_temp)

elif unit == 'c' or unit == 'C':
    new_temp = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit =", new_temp)

else:
    print("Invalid unit")
