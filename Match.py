# match in python (it is a switch)

day = int(input("Enter week day number: "))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Enter valid number..")  

# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

'''
Note:
    The value _ will always match, so it is important to place it as the last case to 
    make it behave as a default case.
'''