# Write a Python program to create series from array using Panda and 
# Write a Python program to create series from list using Panda and Write 
# a Python program to access element of series using Panda. 

import pandas as pd

series = pd.Series([1,2,3,4,5])

for i in range(len(series)):
    print(series[i])