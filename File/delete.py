import os

if os.path.exists("bittu.txt"):
    os.remove("bittu.txt")
    print("file deleted") 
else:
    print("The file does not exist")

    