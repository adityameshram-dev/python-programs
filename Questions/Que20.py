# write a program to Print the number in words 
# for Example: 1234 => One Two Three Four.

num = input("Enter a number: ")

words = ("Zero","One","Two","Three","Four",
         "Five","Six","Seven","Eight","Nine")

for digit in num:
    print(words[int(digit)], end=" ")