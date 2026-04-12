# Write a program to check if the input year is a leap year of not,

yr = int(input("Enter year: "))

if (yr%4==0 and yr%100!=0) or yr%400==0:
    print(f"{yr} is leap year")
else:
    print(f"{yr} is not leap year")
