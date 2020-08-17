list = [1, 2, 3, 4, 5, 6]
print(list)
# It will assign value to the value to the second index
list[2] = 10
print(list)
# Adding multiple-element
list[1:3] = [89, 78]
print(list)
# It will add value at the end of the list
list[-1] = 25
print(list)

#The list elements can also be deleted by using the del keyword.
# Python also provides us the remove() method if we do not know
# which element is to be deleted from the list.

list = [1, 2, 3, 4, 5, 6]
print("before deltion ",list)
list.remove(2)
# It will assign value to the value to second index
print("after deltion ",list)
# Adding multiple element
list[1:3] = [89, 78]
print(list)
# It will add value at the end of the list
list[-1] = 25
print(list)