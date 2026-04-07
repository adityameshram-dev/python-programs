# map() Function 

num = [1,2,3,4]

sq = map(lambda x : x**2, num)
print(list(sq))

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax
# map(function, iterables)
# function that perform operation on element
# An iterable is an object that can be looped over (iterated) element by element.
