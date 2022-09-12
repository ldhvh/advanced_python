import math
#task1
name=str(input("Your last and first name?"))
age=int(input("How old are you?"))
phone=str(input("Your phone number?"))
print("Your last and first name are",name)
print("Your age is",age)
print("Your phone number",phone)
#task2
print( "press 1 for rectangle, 2 for circle and 3 for triangle" ) 
figure=input()

if figure=='1':
    a=float(input("a = ")) 
    b=float(input("b = ")) 
    print("area is",str(round(a*b,2))) 
elif figure=='2' : 
    r=float(input("r = "))
    print("area is",str(round(pi * r ** 2,2))) 
elif figure=='3' : 
    a=float(input("a = ")) 
    b=float(input("b = ")) 
    c=float(input("c = ")) 
    p=(a + b + c)/2 
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    print("area is",str(round(s,2)))
#task4
b=float(input("enter A: "))
a=b*b
res=(a/3)+((a+4)/6)+(math.sqrt(a+4)/4)+((math.sqrt(a+4)**3)/4)
print(res)
#task5
print("Multiply the number by 5, add8 and multiply the sum by 2")
a=float(input())
