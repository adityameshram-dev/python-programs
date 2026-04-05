age = int(input("Enter age: "))

print("you are not a teenager") if age >= 20 else ( print("you are a teenager") if age <= 19 and age >= 13 else print("your are a kid") )

# syntax
# [excute_if_condition_true] if [condition] else [excute_if_condition_false]