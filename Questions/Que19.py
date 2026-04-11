# Write a Python program to find the repeated items of a tuple

tp = (1, 2, 1, 2, 3, 4, 5, 2, 3)

repeated = []

for i in range(len(tp)):
    for j in range(i + 1, len(tp)):
        if tp[i] == tp[j] and tp[i] not in repeated:
            repeated.append(tp[i])

print("Repeated items are:", repeated)