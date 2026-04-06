a=5     #int
b=5.5   #float
c=1+5j  #complex

x=float(a) 
z=complex(b)
y=int(c.real)   #complex number not convert direct to int , only real part 

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)
