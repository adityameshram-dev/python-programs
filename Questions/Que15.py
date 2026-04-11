# Write a python program to find Factorial of given number.

num = int(input("Enter number: "))
fact = 1
for i in range(1,num+1):
    fact = fact  * i
    i = i + 1

print(f"Factorial of {num} is: {fact}")    
