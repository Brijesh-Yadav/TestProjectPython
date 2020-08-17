
lucky_num = [1,2,3,4]
friends = ["kevin","Karen","jim"];

print(friends);
#add two list together
#friends.extend(lucky_num);

print("friends extended with ",friends)

#add new element to friend list
friends.append("Jammi")
print("after adding new element to last",friends)

#insert element in the middle
friends.insert(1,"sam")
print("After insert", friends)

#clear() method clear all the element in the object
#friends.clear()

#pop() method removes the last element of the list
friends.pop()
print("After pop", friends)

#index() method is used to chek the present in the list
print(friends.index("sam"))

#method list
#count()
print("count() ",friends.count("sam"));
#sort()
print("sort()",lucky_num.sort());
#reverse()
print("reverse() ",lucky_num.reverse());

#copy() - it is used to copy element from 1 objec to another
friends2 = friends.copy();
print(friends2)