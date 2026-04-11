# Write a program to calculate perimeter and area of a cylinder, rectangle and square. 

import math
PI = math.pi

def rectangle(l,w):
    print("Perimeter: ", 2 * (l + w))
    print("Area: ",l * w)

def square(s):
    print("Perimeter: ", 4 * s)
    print("Area: ",s**2)

def cylinder(r,h):
    print("Perimeter: ", 2 * PI * r)
    print("Area: ", 2 * PI * r * (r + h))


print("Enter length and width: ")
l,w = map(float,input().split(" "))

print("Enter side: " )
s = float(input())

print("Enter Radius and Height: ")
r,h = map(float,(input()).split(" "))

rectangle(l,w)
square(s)
cylinder(r,h)





