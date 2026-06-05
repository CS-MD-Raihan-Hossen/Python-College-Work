import math
a=float(input('Enter the Value a:' ))
b=float(input('Enter the Value b:' ))
c=float(input('Enter the Value c:'))

d=(b**2)-(4*a*c)
# d=int(d)
# print(d)
# print(math.sqrt(d))
x1=(b+math.sqrt(d))/(2*a)
x2=(b-math.sqrt(d))/(2*a)

print("Equation One: ",x1)
print("Equation One: ",x2)

