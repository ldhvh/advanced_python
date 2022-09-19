import math
#1
a=int(input("enter a "))
b=int(input("enter b "))
h=int(input("enter h "))
s=(((a**(2)+b)*h)/(2*(a-b)+4))
print("area is ",str(round(s,2)))
#2
x=int(input("enter x "))
y=int(input("enter y "))
h=math.sqrt(math.cos(2*y)+math.sin(4*y)+math.sqrt(math.e**(x)+math.e**(-x)))/((math.pow(math.e**(-x)+math.e**(x),3)*(math.pow(math.sin(4*y)+math.cos(2*y)-2,2))))
print("H is ",str(round(h,2)))
print()
#3(1)
x=2
y=1
res=x**x*y+math.pow(x,math.pow(x,y))-x**4
print(str(round(res,2)))
#3(2)
x=1
y=4
z=3
res=((math.fabs((1/math.tan(y))+6))**(1/3)+math.sqrt(((x+1)**3)/(4*y - 2*z)))
print(str(round(res,2)))
#3(3)
x=3
y=0.2
res=(((5*x*y)/((x**3)-4))+math.exp(x**2)+math.sqrt((math.cos(y))**2-y**2))
print(str(round(res,2)))
#3(4)
x=3
y=5
res=(math.sqrt(math.fabs(y))+((math.atan(math.log(x))**3)/((x**(y))-y+1)))
print(str(round(res,2)))
#3.2(1)
x=3
y=1
z=2
res=math.pow(4,x*y)-math.pow(x,y*z)+math.pow(x*y,z)
print(str(round(res,2)))
#3.2(2)
x=2
y=2
z=1
res=((4*math.fabs(x))-x*y*math.pow(z,2))/(x+math.exp(y*x)-2*y*z)
print(str(round(res,2)))
#3.2(3)
x=0.8
y=0.1
z=4
res=((1-x+(1/math.atan(x-7*y)))/(4*x*z-math.pow(math.log(y),2)))**(1/5)
print(str(round(res,2)))
#3.2(4)
x=3
y=1
z=3
res=(2*3*4)/(math.pow(math.sin(x),3)+math.pow(math.tan(y),3))-(math.sqrt(math.pow(z,x-y)))
print(str(round(res,2)))
#3.3(1)
x=4
res=(math.pow(math.log(x-3),4)+2**(x)*math.pow(math.sin(3*x),2))/(4*x-5.2)
print(str(round(res,2)))
#3.3(2)
x=2
y=2
z=1
res=math.sqrt(0.6*x*y*z)+y**(2*x)-math.exp(math.sin(2*math.pow(x,2)))
print(str(round(res,2)))
#3.3(3)
x=0.5
y=2.0
res=(math.asin(math.pow(x,3))-6)/(8*(math.cos(4*y)-math.sin(4*x)))
print(str(round(res,2)))
#3.3(4)
x=2
y=1
z=3
res=(math.fabs(math.log(x**3))+math.exp(2*x))/(x+3.4)-(math.pow((1/(math.tan(3/(x*y*z)))),3))
print(str(round(res,2)))
print()
#2(area)
a=int(input("enter a: "))
b=int(input("enter b: "))
c=math.sqrt((a**2) + (b**2))
s=(a*b)/2
p=a+b+c
print("area is {0:.2f}".format(s))
print("perimeter is {0:.2f}".format(p))

#3(roots)
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
d=(b**2)-4*a*c
if d>0:
    x1=((-b)+math.sqrt(d))/(2*a)
    x2=((-b)-math.sqrt(d))/(2*a)
    print("root one is ",x1)
    print("root two is ",x2)
elif d==0:
    x1=(-b)/(2*a)
    print("root is ",x1)
else:
    print("no roots")
#4(areas)
print( "press 1 for rectangle, 2 for circle and 3 for triangle" ) 
figure=input()

if figure=='1':
    a=float(input("a = "))
    b=float(input("b = "))
    print("area is",round(a*b,2))
elif figure=='2' : 
    r=float(input("r = "))
    print("area is",round(math.pi * r ** 2,2))
elif figure=='3' : 
    a=float(input("a = "))
    b=float(input("b = "))
    c=float(input("c = "))
    p=(a + b + c)/2 
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("area is",round(s,2))
