# built-in Exception

a = [1,2,3,4]
fruit = {"name": "apple", "color": "red"}
s  = "bittu"
   
try:
    from math import xyz
except ImportError:          # An ImportError will occur when you try to import a non-existing part of a module:
    print("Error: Import module proper")

try:
    print(a[5])
except IndexError:          # An IndexError occurs if you try access a list item with an index that does not exist:
    print("Error: You try to acces that dose not exit..")

try:
    print(fruit["price"])
except KeyError:            # A KeyError occurs if you try access a dictionary with a key that does not exist:
    print("Error: Key does not Exit")   

try:
    print(di)
except NameError:
    print("Error: Variable dose not Exit..")
    
try:
    print(s + 15)
except  TypeError:
    print("Error: Can't Add string and number..")
    






