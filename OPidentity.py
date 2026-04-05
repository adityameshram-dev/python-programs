# python Identity operator

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)


print(x is y)


print(x is not y)

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
# == check value from variable
# is check memory location

# used to check memory location of object