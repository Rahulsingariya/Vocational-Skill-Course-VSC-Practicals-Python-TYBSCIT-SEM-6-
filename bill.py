print("Price of pen is 5rs")
print("Price of pencil is 3rs")
print("Price of eraser is 3rs")
print("Price of scale is 5rs")
print("Price of sharpner is 3rs")


pen = int(input("Enter the quantity of pen:"))
pencil  = int(input("Enter the quantity of pencil:"))
eraser = int(input("Enter the quantity of eraser:"))
scale  = int(input("Enter the quantity of scale:"))
sharpner = int(input("Enter the quantity of sharpner:"))

total_amount_of_pen = 5*pen
total_amount_of_pencil = 3*pencil
total_amount_of_eraser = 3*eraser
total_amount_of_scale = 5*scale
total_amount_of_sharpner = 3*sharpner

print("Total amount of pen is:",total_amount_of_pen)
print("Total amount of pencil is:",total_amount_of_pencil)
print("Total amount of eraser is:",total_amount_of_eraser)
print("Total amount of scale is:",total_amount_of_scale)
print("Total amount of sharpner is:",total_amount_of_sharpner)

total_amount = total_amount_of_pen+total_amount_of_pencil+total_amount_of_eraser+total_amount_of_scale+total_amount_of_sharpner

print("Total amount:",total_amount)
discount = total_amount * (10/100)
print("Discount of 10%:",discount)
discounted_amount = total_amount-discount

print("Total amount with 10% discount:",discounted_amount)

tax =  discounted_amount + (5/100)

print("Total amount including 5% tax after discount:", tax)








