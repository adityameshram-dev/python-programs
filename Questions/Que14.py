# Write a Python Program to Reverse a given number 

num = int(input("Enter number: "))

temp = num
rev = 0
while(temp > 0):
    rem = temp % 10
    rev = rev*10 + rem
    temp = temp // 10

print("Reverse number: ", rev)