class student:
    def __init__(self, name,roll,clg):
        self.name = name
        self.roll = roll
        self.clg = clg
    def display(self):
        print("name: ",self.name)
        print("roll: ",self.roll)
        print("college: ",self.clg)

s1 = student("Bittu",45,"GPS")
s1.display()