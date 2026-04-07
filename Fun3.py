# Function with argument and with return value

def fibo(n):
    f1, f2 = 0, 1
    result = []
    for i in range(n):
        result.append(f1)
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return result

print(fibo(10))