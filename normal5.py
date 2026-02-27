temp = float(input())
unit = input()

if unit == "f":
    new_temp = (temp - 32)*5/9
    new_unit = "c"

else:
    new_temp = (temp * 9/5) + 32
    new_unit = "f"

print(temp,unit,"is converted to",new_temp,new_unit)
