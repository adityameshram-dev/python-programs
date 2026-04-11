# Write Python program to read and print students information using single inheritance.

class student:
    def accept(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll number: "))

class displayinfo(student):
    def display(self):
        print(f"name: {self.name}")
        print(f"roll: {self.roll}")

d1 = displayinfo()
d1.accept()
d1.display()