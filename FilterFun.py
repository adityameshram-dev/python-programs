# fliter function

marks = [70, 67, 97, 92, 68, 82]

def checkmarks(x):
  if x < 80:
    return False
  else:
    return True

adults = filter(checkmarks, marks)

for x in adults:
  print(x)

# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# Keeps element → if function returns True
# Skips element → if function returns False  