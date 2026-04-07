# pass by refference

def change_list(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [1, 2, 3]
change_list(my_list)
print("Outside function:", my_list)

# Mutable data types (list, set, dictionary) can be changed inside a function, so they behave like pass by reference


# pass by value

def change(x):
    x = x + 3
    print("inside x value: ", x)
x = 2
change(x)
print("outside x value: ", x)

# Immutable data types (int, float, string, tuple) cannot be changed, so they behave like pass by value.