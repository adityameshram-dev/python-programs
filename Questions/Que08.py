# Write a program that takes the marks of 5 subjects and displays the grades 

m1,m2,m3,m4,m5 = map(int,input("Enter 5 subject mark ").split())

per = (m1+m2+m3+m4+m5)/5.0
if per <= 100 and per >= 80:
    print("Frist class..")
elif per <= 79 and per >= 60:
    print("Second class..")    
elif per <= 59 and per >= 40:
    print("pass..")
else:
    print("Fail..")    
print(per)