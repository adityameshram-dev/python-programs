class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"

s1 = student("bittu",19)        
print(s1)

# The __str__() method is a special method that controls what is returned when the object is printed