# Reading from file in python using read mode

# there are two ways to read file

# First way

try:
    f = open("bittu.txt")
    data = f.read()
    print(data)
except Exception as e:
    print("Error: ", e)
finally:
    print("\n\nRead from file..\n\n")
    f.close()

# Second way

try:
    with open("bittu.txt") as f:
        data = f.read()
        print(data)
        print("Read from file..")
except Exception as e:
    print("Error: ", e)

# No need to use close() it close automatic

''' NOTE '''
# "r" mode (read mode):
# By default, file opens in "r" (read) mode
# - File must exist, otherwise gives error
# - Does not modify the file