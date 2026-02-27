hour = int(input("Enter the time :"))
if hour < 8:
    print("Too Early")
elif hour < 12:
    print("Good Morning")
elif hour < 13:
    print("Lunchtime")
elif hour < 17:
    print("Good Afternoon")
else:
    print("Too Late")
