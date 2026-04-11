# Write a Python program that takes a number and checks whether it is a palindrome or not. 

num = int(input("Enter number: "))

temp = num
rev = 0
while(temp > 0):
    rem = temp % 10
    rev = rev*10 + rem
    temp = temp // 10
if rev == num:
    print(f"{num} is palindrome")  
else:
    print(f"{num} is not palindrome") 
      
    