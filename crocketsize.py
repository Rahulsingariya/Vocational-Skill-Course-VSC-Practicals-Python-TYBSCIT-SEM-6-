size = input("Enter crochet hook size: ")

diameter = -1.0

if size == 'a':
    diameter = 3.25
elif size == 'b':
    diameter = 2.25
elif size == 'c':
    diameter = 2.75
elif size == 'd':
    diameter = 3.5
elif size == 'f':
    diameter = 3.75
elif size == 'g' or size == 'G':
    diameter = 4.0

print("Metric diameter =", diameter)
