# Write a Python function that accepts a string and calculate the 
# number of upper case letters and lower case letters. 

def cal(name):
    countU , countL = 0 , 0
    
    for i in name:
        if i.islower():
            countL += 1
        elif i.isupper():
            countU += 1
    print("Lower case", countL)            
    print("Upper case", countU)

cal("BittU")   