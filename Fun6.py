# Function with Variable-Length Arguments (*args)

def greet(*names):
    print(names)

greet("name","bittu","meshram")

greet(1,2,3,4,5,6,"bittu")

# When you don't know how many items a user might pass 
# (like a list of numbers to sum), use *args. 
# This collects extra positional arguments into a tuple.