# Write a Python program to implement multilevel inheritance. 

class Grandfather:
    def show_grandfather(self):
        print("I am Grandfather")

class Father(Grandfather):
    def show_father(self):
        print("I am Father")

class Child(Father):   # multilevel inheritance
    def show_child(self):
        print("I am Child")


# Object create
c1 = Child()

c1.show_grandfather()
c1.show_father()
c1.show_child()