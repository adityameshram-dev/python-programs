# ZeroDivisionError in Exception 

a, b = 5, 0

try:
    div = a / b
    print(div)
except ZeroDivisionError:
    print("Divided by Zero Exception")    


# The ZeroDivisionError exception occurs when we try to devide a number with 0, and when we perform a modulo operation with 0.
# The ZeroDivisionError exception is one of three ArithmeticError    