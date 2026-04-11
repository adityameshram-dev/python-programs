# Write a program to find sum of four digit number.

num = int(input("Enter number: "))
sum = 0

while num > 0:
    rem = num%10
    sum = sum + rem
    num //= 10

print(f"sum of digit is ",sum)