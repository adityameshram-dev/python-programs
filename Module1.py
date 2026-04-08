# user define modele

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "error"
    else:
        return a/b

# In Python, a module is simply a file that contains code 
# (functions, variables, classes) which we can reuse in other programs.        

''' This is a user difine module in another file we import this module '''