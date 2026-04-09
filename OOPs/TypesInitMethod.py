class clg:
    def __init__(self):
        print("Default Constructor called")

class emp:
    def __init__(self,name):
        self.name = name
        print("parameterised constructor called")
        print(f"my name is {self.name}")

c1 = clg()
e1 = emp("bittu")

# Multiple constructors Not allowed in python 

