my_list = [10, 40, 20, 50, 30]
print("Original List:", my_list)
print("Element at zeroth index:", my_list[0])
print("Element at first index:", my_list[1])
my_list.insert(3, 60)
print("List after inserting 60 at index 3:", my_list)
my_list.pop(2)
print("List after removing element at index 2:", my_list)
del my_list[1]
print("List after deleting element at index 1:", my_list)
my_list.sort()
print("Sorted List:", my_list)
print("Elements with index positions:")
for index, value in enumerate(my_list):
    print("Index", index, ":", value)
