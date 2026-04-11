# Write a Python program to implement multiple inheritance.

class Father:
    def skills_father(self):
        print("Father: Farming Skills")

class Mother:
    def skills_mother(self):
        print("Mother: Cooking Skills")

class Child(Father, Mother):   # multiple inheritance
    def skills_child(self):
        print("Child: Sports Skills")


# Object create
c1 = Child()

c1.skills_father()
c1.skills_mother()
c1.skills_child()