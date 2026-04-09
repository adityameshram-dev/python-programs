class student:
    def accept(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name)
        print(self.roll)

class result(student):
    def accept1(self,m1,m2,m3,m4):
        self.m1,self.m2,self.m3,self.m4 = m1,m2,m3,m4

    def display1(self):
        print(self.m1+self.m2,self.m3+self.m4/4)

r1 = result()
r1.accept("bittu",45)
r1.accept1(100,100,55,70)
r1.display()
r1.display1()