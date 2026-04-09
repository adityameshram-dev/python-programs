class Myclass:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

o1 = Myclass("bittu",18)
o2 = Myclass("aditya",19)

print(o1.name)
print(o2.age)

# The __init__() method is called automatically every time the class is being used to create a new object.
# The __init__() metgod is also called as Constructor