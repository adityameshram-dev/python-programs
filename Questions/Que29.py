# Write a program to use map and reduce function. 

from functools import reduce

num = [1, 2, 3, 4, 5]

sq = list(map(lambda x: x * x, num))
print("Squares using map:", sq)

sum = reduce(lambda x, y: x + y, num)
print("Sum using reduce:", sum)