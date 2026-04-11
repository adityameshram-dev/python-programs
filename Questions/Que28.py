# Write a program showing both keyword and positional arguments in single function. 

def fun(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


fun("Aditya", 19, "java")
fun(course="Python", name="Aditya", age=19)