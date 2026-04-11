# create a file in python 

try:
    f = open("bittu.txt","x")
    print("File is create")
except FileExistsError as e:
    print("Error: ", e)

# The open() function takes two parameters i.e filename, and mode.    
# "x" - Create : Creates the specified file, returns an error if the file exists