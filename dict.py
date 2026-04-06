d = {"name": "Bittu", "age": 25, "city": "Mumbai"}

# print specific value by key
print(d["age"])

# print all keys
print("Keys: ",d.keys())

# print all values
print("Values:", d.values())

# print all key value pair
print("Keys and values", d.items())

# Loop through keys, by using the keys() method:
print("\nLoop through keys : ")
for i in d.keys():
    print(i,end = " ")

# Loop through values, by using the values() method:
print("\nLoop through values: ")
for j in d.values():
    print(j, end=" ")

# Loop through both keys and values, by using the items() method:
print("\nLoop through keys and values: ")
for key,value in d.items():
    print(f"{key}:{value}", end= ", ")


# Dictionary is a data structure in Python
# Dictionary stores data in key-value pairs
# Dictionary is unordered (but from Python 3.7+ it maintains insertion order)
# Dictionary is mutable in Python
# Dictionary does NOT allow duplicate keys (values can be duplicate)
# Dictionary allows heterogeneous data (different data types)
# Dictionary data is accessed using keys (not index)
# Example: dict["name"]
# Dictionary keys must be unique and immutable (like string, int, tuple)
# Dictionary is dynamic and growable
# Dictionary is iterable (loops through keys by default)
# Dictionary supports nesting (dictionary inside dictionary)