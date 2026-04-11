# Write a Python program to perform following operations on set: 
# intersection of sets, union of sets, set difference, symmetric difference, clear a set

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print("Intersection: ", s1.intersection(s2))
print("Union: ", s1.union(s2))
print("Difference: ",s1.difference(s2))
print("symmetric differenc",s1.symmetric_difference(s2))
print(s1.clear())
print(s2.clear())