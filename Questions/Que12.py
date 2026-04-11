# Print the following patterns using loop: 

'''
1010101 
 10101 
  101 
   1
'''

for i in range(4):             

    for j in range(i):         
        print(" ", end="")

    for k in range(7 - 2*i):
        if k % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")

    print()

        