# Write a Python program to create a class 'Degree' having a method 
# 'getDegree' that prints "I got a degree". It has two subclasses namely 
# 'Undergraduate' and Postgraduate' each having amethod with the same 
# name that prints "I am an Undergraduate" and "I am a Postgraduate" 
# respectively. Call the method by creating an object of each of the three classes. 

class Degree:
    def getDegree(self):
        print("I got a degree")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")


d1 = Degree()        
u1 = Undergraduate()
p1 = Postgraduate()

d1.getDegree()
u1.getDegree()
p1.getDegree()
    