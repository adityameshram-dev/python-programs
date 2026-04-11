# else and finally in Exception

''' else '''

try:
    print("hello")
except:
    print("Error: Something Error occur...")    
else:
    print("Everything is fine..")  

# if except block is not execute else block execute 
# if except block is execute else block is not exeute


''' finally '''

try:
    div = 5 / 0
    print(div)
except ZeroDivisionError:
    print("Can't Divided by Zero..")    
else:
    print("This block not execute..")    
finally:
    print("This block execute..")    

# finally block is always execute Whether an error occurs or not
