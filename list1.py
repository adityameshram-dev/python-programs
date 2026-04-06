# list method 

a = [9,7,5,3,1,]
b = [1,2,3,4,5]

print(a.pop())    # pop() used to delete last element from the list and it return pop element

a.append(11)      # append() used to insert an element at last position of list
print(a)

a.insert(5,13)    # insert(index,element) used to insert an element into list 
print(a)

a.reverse()       # reverse() used to reverse the element from the list
print(a)

a.sort()          # sort() used to sort the element from the list
print(a)

b=a.copy()        # copy() used to copy the list one to another list if a list content some element so delete the all element from the list and put new element
print(b)

a.extend(b)       # extend() used to add multipal element in list
print(a)

b.clear()         # clear() used to removes all the elements from a list.

print(min(a))    # min() used to find minimum value from list

print(max(a))    # max() used to find maxmimum value from list


