# Write a program to swap the value of two variables. 

a,b = map(int,input("Enter two number: ").split(" "))

print("befour swap")
print(f"a = {a} and b = {b}")
a = a + b
b = a - b
a = a - b
print("after swap")
print(f"a = {a} and b = {b}")