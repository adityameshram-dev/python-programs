class Myclass:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def greet(self):
        print(f"My name is {self.name} and yours ?")

obj = Myclass("bittu",19)        
obj.greet()

# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# The self parameter must be the first parameter of any method in the class.
# it does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class

