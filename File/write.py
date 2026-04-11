# Writing into file in python 

# there are two ways to write into file

# First way

try:
    f = open("Aditya.txt", "w")
    f.write("Hi my name is Aditya\n")
    f.write("I'm student of GPS")
except  Exception as e:
    print("Error: ", e)
finally:
    print("Written in file..")
    f.close()

# Second way

try:
    with open("bittu.txt" , "w") as f:
        f.write("I start learing python and it feel so easy to improve my skill..")
        print("Written in file..")
except  Exception as e:
    print("Error: ", e)

# No need to use close() it close automatic

''' NOTE '''
# "w" mode (write mode):
# - Opens file for writing
# - Creates file if it does not exist
# - Overwrites file if it already exists



        