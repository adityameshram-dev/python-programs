# Write a Python class that has two methods: get_String and 
# print_String, get_String accept a string from the user and print_String 
# prints the string in upper case. 

class string:
    def get_String(self):
        self.name = input("Enter a String: ")

    def print_String(self):
        print(self.name.upper())

s1 = string()
s1.get_String()
s1.print_String()

