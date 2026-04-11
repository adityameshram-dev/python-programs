# Print the following patterns using loop: 

'''
     * 
    *** 
   ***** 
    *** 
     *
'''

for i in range(3):
    for j in range(3 - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(3 - 2, -1, -1):
    for j in range(3 - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()