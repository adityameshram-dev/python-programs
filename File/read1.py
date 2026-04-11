# Reading from file in python using read mode

with open("bittu.txt") as f:
    print(f.readline())
# it read only one line from file

# read file with loop
with open("bittu.txt") as f:
    for x in f:
        print(x,end=" ")