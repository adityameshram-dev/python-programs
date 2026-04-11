# Raise an exception

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Your age is bellow 18")
    else:
        print("you can vote")
except ValueError as e:
    print("Error: ", e)      


# The raise keyword is used to raise an exception.  
# We can give an alias to the exception using 'as'