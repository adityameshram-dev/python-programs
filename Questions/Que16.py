# Write a python program to find Fibonacci series for given number

term = int(input("Enter number: "))
f1, f2 = 0, 1

for i in range(term+1):
    f3 = f1+f2
    print(f1 , end= "")
    f1,f2 = f2,f3