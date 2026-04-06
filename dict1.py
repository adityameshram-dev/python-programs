d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

d1 = d.copy()         # Make a copy of a dictionary with the copy() method:
print("d1: ", d1)

print(d.get("brand"))   # The get() method returns the value of the item with the specified key.

print(d.items())        # The items() method returns a view object.

print(d.keys())         # The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

d.pop("year")         # The pop() method removes the specified item from the dictionary.
print(d)

d.popitem()         # The popitem() method removes the item that was last inserted into the dictionary. 
print(d)

print(d.setdefault("price", "10M")) # The setdefault() method returns the value of the item with the specified key.

# Change the value

d["model"] = "BMW"
print(d)

d2 = dict(d1)               # Make a copy of a dictionary with the dict() function: 
print("d2", d2)

d.update({"year": 2006})      # Change the value using update() method
print(d)

# Add Key and value
d["color"] = "black"
print(d)

# Add Key and value using update() method
d.update({"price":"1M"})
print(d)

# The del keyword removes the item with the specified key name
del d["year"]
print(d)


# Note
'''
The del keyword can also delete the dictionary completely: example del d
Use del() when you're certain the element exists
Use pop() when you're not sure, or to avoid errors
'''