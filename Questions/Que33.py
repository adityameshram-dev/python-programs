# Write a python program to implement parameterized constructor.

class constructor:
    def __init__(self, id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")

c1 = constructor(45,"Aditya",19)
c1.display()