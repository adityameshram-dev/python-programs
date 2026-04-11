#  Write a program to check the largest number among the three numbers using if-else. 

a, b, c = map(int,input("Enter 3 number: ").split(" "))

if a>b and a>c:
    print(f"{a} is largest number among {b} and {c}")
elif b>a and b>c:
    print(f"{b} is largest number among {a} and {c}")
else:
    print(f"{c} is largest number among {a} and {b}")    
