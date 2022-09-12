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
c=((a/2)-8)/5
print(c)
#task2.1
a = int(input('enter the first number: '))
b = input('input operation(+,-,*,/): ')
c = int(input('enter the second number: '))

switcher={
"+": print(a+c),
"-": print(a-c),
"*": print(a*c),
"/": print(a/c),
"%": print(a%b),
"//": print(a//c)
    }
switcher.get(b,"err")

#task2.2
a = int(input('enter the first number: '))
b = input('input operation(+,-,*,/): ')
c = int(input('enter the second number: '))
switcher={
"+": print(a+c),
"-": print(a-c),
"*": print(a*c),
"/": print(a/c),
"%": print(a%b),
"//": print(a//c)
    }
if c==0:
    print("no dividing by zero.")
    c = int(input('enter the second number: '))
    else
switcher.get(b,"err")
#task2.4
start = 34
end = 67
for num in range(start, end):
    if num % 2 == 0:
        print(num, end = " ")
#task2.5
#guessing
name = "Leila"
c = 0
while True:
    n = input("Enter name: ").lower()
    c = c + 1
    if n == name:
        break
    if n != name and c > 7: 
        break
