import math
#ex1
def printChar(s):
    print(s)
sim = input('enter symbol: ')
printChar(sim)
printChar('*')

#ex2
x=3
def pr():
    print(x)
pr()
def pa(a)
    print(a)
pa(a)
x=3
print('Starting value: ',x)
def pr():
    global x
    x=pow(x,10)
    print('Changed value',x)
pr()
#function ex
def sumD(n):
    summa = 0
    while n!=0:
        summa+= n%10
        n=n//10
    return summa
print (sumD(int(input())))
#task0.1
def s(x,y,z):
    p=(x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s
A=[]
for i in range(3):
    print('Enter sides of ',i,'-sided triangle')
    a=int(input('a: '))
    b=int(input('b: '))
    c=int(input('c: '))
    A.append(s(a,b,c))
for i in range(3):
    print('Area of ',i,'-sided triangle')
if A[0]==A[1]:
    if A[0}==A[2]:
        print('Triangles are equal')
else: print('Triangles are not equal')
#task0.2
def zam(X):
    tmp = X[0]
    X[0]=X[len(X)-1]
    X[len(X)-1]=tmp
A=[]
m=int(input('Enter array length: '))
for i in range(m):
    print('Enter ',i,'th element of the array')
    A.append(int(input()))
print(A)
zam(A)
print(A)
