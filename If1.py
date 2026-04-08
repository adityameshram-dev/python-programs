# nested if in python 

print("enter number: ")
a=int(input())

if a%2==0:
    if a>0:
        print(a,"is a positive even number")
    else:
        print(a,"is a negtive even number")
else:
    if a>0:
        print(a,"is positive odd number")  
    else:
        print(a,"is negtive odd number")