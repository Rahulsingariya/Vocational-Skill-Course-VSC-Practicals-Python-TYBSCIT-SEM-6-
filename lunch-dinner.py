menu = input("Enter menu (lunch/dinner): ")
choice = int(input("Enter meal choice (1, 2, or 3): "))

if menu == "lunch":
    if choice == 1:
        print("Caesar Salad")
    elif choice == 2:
        print("Spicy Chicken Wrap")
    elif choice == 3:
        print("Butternut Squash Soup")
    else:
        print("Invalid meal choice")

elif menu == "dinner":
    if choice == 1:
        print("Baked Salmon")
    elif choice == 2:
        print("Turkey Burger")
    elif choice == 3:
        print("Mushroom Risotto")
    else:
        print("Invalid meal choice")

else:
    print("Invalid menu choice")
