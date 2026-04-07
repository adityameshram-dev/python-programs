# Built-in Function in python 

a = 5
print(type(a))  # The type() function returns the type of the object passed to type function.

s = "Bittu"
print(len(s))   # The len() function returns the number of items in an object.

for i in range(1,10,2):
    print(i)

# Syntax
# range(start, stop, step)
# The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number.


l = [1,2,3,4,5]
l1 = reversed(l)        # The reversed() function returns a reversed iterator object.
print(list(l1))

t1 = (5,4,3,2,1)
print(sorted(t1))       # The sorted() function returns a sorted list of the specified iterable object.

''' Note: We cannot sort a list that contains BOTH string values AND numeric values '''






