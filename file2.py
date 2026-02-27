filename = input("Enter file name with extension: ")

try:
    file = open(filename, "r")
    print("File found. Contents of the file are:\n")
    
    for line in file:
        print(line, end="")
    
    file.close()
