# Writing into file in python using append mode

# there are two ways to append into file

# First way

try:
    f = open("bittu.txt", "a")
    f.write("\nHi my name is Aditya")
    f.write("\nI'm student of GPS")
except Exception as e:
    print("Error: ", e)
finally:
    print("Appended in file..")
    f.close()

# Second way

try:
    with open("bittu.txt", "a") as f:
        f.write("\nI started learning python and it feels easy to improve my skills..")
        print("Appended in file..")
except Exception as e:
    print("Error: ", e)

# No need to use close() it close automatic

''' NOTE '''
# "a" mode (append mode):
# - Opens file for appending
# - Creates file if it does not exist
# - Adds new data at the end of file without deleting old data