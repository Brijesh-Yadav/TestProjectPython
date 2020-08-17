#A tuple is similar to the list in many ways. Like lists,
# tuples also contain the collection of the items of different data types.
# The items of the tuple are separated with a comma (,)
# and enclosed in parentheses ().

#A tuple is a read-only data structure as we can't modify the size
# and value of the items of a tuple.

tup = ("hi", "Python", 2)
# Checking type of tup
print(type(tup))

# Printing the tuple
print(tup)

# Tuple slicing
print(tup[1:])
print(tup[0:1])

# Tuple concatenation using + operator
print(tup + tup)

# Tuple repatation using * operator
print(tup * 3)

# Adding value to tup. It will throw an error.
print[2] = "hi"