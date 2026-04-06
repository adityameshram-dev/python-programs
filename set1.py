s = {"bittu","GP sakoli",45,90.35}
s1 = {"aditya","meshram",44,90.45}
s2 = {}

# set method

s.add("python")         # The add() method adds an element to the set. 
print(s)                # If the element already exists, the add() method does not add the element.

print(s.pop())             # Removes a randome element form set and returns removed value.

s.remove(45)                # The remove() method removes the specified element from the set.
print(s)         

s.discard(90.35)            # The discard() method removes the specified item from the set.
print(s)

s2 = s.copy()               # The copy() method copies the set
print(s)

s2.clear()                  # The clear() method removes all elements in a set.
print(s2)


print(s.union(s1))          # Return a set containing the union of sets 

print(s.intersection(s1))   # Returns a set, that is the intersection of two other sets 


# Note

'''
Use remove() when you're certain the element exists it may throw error
Use discard() when you're not sure, or to avoid errors
'''