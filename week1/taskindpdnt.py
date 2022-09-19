import math
#task1
name=str(input("Your last and first name? "))
age=int(input("How old are you? "))
phone=str(input("Your phone number? "))
print("Your last and first name are ",name)
print("Your age is ",age)
print("Your phone number ",phone)
#task2
print()
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
#task4
print()
b=float(input("enter A: "))
a=b*b
res=(a/3)+((a+4)/6)+(math.sqrt(a+4)/4)+((math.sqrt(a+4)**3)/4)
print("{0:.2f}".format(res))
#task5
print()
print("Multiply the number by 5, add 8 and multiply the sum by 2: ")
a=float(input())
c=((a/2)-8)/5
print(c)
#task2.1
print()
a = int(input('enter the first number: '))
b = str(input('input operation(+,-,*,/): '))
c = int(input('enter the second number: '))

def switch(a,b,c):
        if b=='+':
            print(a+c),
        if b=='-':
            print(a-c),
        if b=='*':
            print(a*c),
        if b=='/':
            print(a/c),
        if b=='%':
            print(a%c),
        if b=='//':
            print(a//c)
switch(a,b,c)

#task2.2
print()
a = int(input('enter the first number: '))
b = str(input('input operation(+,-,*,/): '))
c = int(input('enter the second number: '))

def switch(a,b,c):
        if b=='+':
            print(a+c),
        if b=='-':
            print(a-c),
        if b=='*':
            print(a*c),
        if b=='/':
            if c==0:
                print("no dividing by zero.")
            else:
                print(a/c),
        if b=='%':
            print(a%c),
        if b=='//':
            print(a//c)
switch(a,b,c)
#task2.3
print()
v = 14
if (v>10 and v!=12 and v>=15) or v==18:
    print("True")
else:
    print("False")
#task2.4
print()
start = 34
end = 67
for num in range(start, end):
    if num % 2 == 0:
        print(num, end = " ")
#task2.5
#guessing
print()
name = "leila"
c = 0
while True:
    n = input("Enter guess name: ").lower()
    c = c + 1
    if n == name:
        print("You guessed right!")
        break
    if n != name and c > 7:
        print("You couldn't guess it. Nice try. ")
        break
#task2.6
print()
i=1
while (i<101):
    if(i==50 or i==99):
        i+=1
    else:
        print(i)
        i+=1
#task2.7
word = input("Enter the word: ")
num = int(input("Enter the number: "))
w_list=list(word)
for i in range(0,len(word)):
    for j in range(0,num):
        print(w_list[i],"")
        j+=1
    print()
    i+=1

    

