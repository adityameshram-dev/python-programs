# Write a Python script to sort (ascending and descending) a dictionary by value.

data = {'a': 30, 'b': 10, 'c': 20}

items = list(data.items())
print(items)

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:   # value compare
            items[i], items[j] = items[j], items[i]

result = dict(items)
print("Ascending:", result)

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1]:   # value compare
            items[i], items[j] = items[j], items[i]

result = dict(items)
print("Descending:", result)
