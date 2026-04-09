# single inheritance

class student:
    def accept(self):
        self.name = input("Enter name: ")
        self.roll = input("Enter roll number: ")
        self.m1, self.m2, self.m3 = map(int,input("Enter 3 subject mark: ").split(" "))
    
class result(student):
    def calculate(self):
        self.avg = (self.m1 + self.m2 + self.m3)/3.0

    def display(self):
        print("Name: ",self.name)
        print("Roll No. ",self.roll)
        print("Average: ", self.avg)

r1 = result()
r1.accept()
r1.calculate()
r1.display()