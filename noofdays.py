start_day = int(input("Enter starting day (1=Mon, 7=Sun): "))
days = int(input("Enter number of days in the month: "))

print("Mon Tue Wed Thu Fri Sat Sun")

for i in range(1, start_day):
    print("    ", end="")

day = 1
current = start_day

while day <= days:
    print(f"{day:3}", end=" ")
    if current == 7:
        print()
        current = 1
    else:
        current += 1
    day += 1
