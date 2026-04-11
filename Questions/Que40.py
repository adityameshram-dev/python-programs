# Write a Python program to create DataFrame using list and dictionary both using Panda.

import pandas as pd

data = {
    "name" : ["bittu", "aditya", "harshal"],
    "age" : [19,19,21],
    "city" : ["nashik", "lakhandur", "nagpur"]
}

df = pd.DataFrame(data)

print(df)
