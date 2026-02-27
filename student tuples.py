import pathlib

roll_num = (19001, 19002, 19003, 19004, 19005)

names = ["Anil", "Haadi", "Sabari", "Numan", "Nihkil"]

print("Roll no:", roll_num)
print("Names :", names)
Show_roll = int(input("Enter roll number to show: "))

filename = open('tyit1.txt','w')
filename.write('Roll No   Name\n')

student_dict = {}

for i in range(len(roll_num)):
    if roll_num[i]==Show_roll:
        student_dict[roll_num[i]] = names[i]

print("Student Dictionary:", student_dict)

filename = open('tyit1.txt','w')
filename.write()
filename.close()

