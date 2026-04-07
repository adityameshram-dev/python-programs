# Function with Keyword Variable-Length Arguments (**kwargs)

def print_info(**kwargs):
    for key,value in kwargs.items():
        print(key, ":" , value)
        

data = {"name": "Aditya", "age": 17, "city": "Nashik"}
print_info(**data)

# it use mainly for dictionary