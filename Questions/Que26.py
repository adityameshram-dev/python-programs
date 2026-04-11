# Write a Python program to find the highest 3 values in a dictionary.

d = {
    5:500,
    4:400,
    3:300,
    2:200,
    6:600,
    1:100
}

top3 = sorted(d.values())
print(top3[:3])