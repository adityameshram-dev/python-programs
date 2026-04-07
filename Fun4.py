# Function without argument and with return value

def fact():
    n = int(input("Enter number to get factorial of that number: "))
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

print(f"factorial of {n} is",fact())    