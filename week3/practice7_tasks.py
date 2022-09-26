import math
#task1.1
def rec():
    a=float(input("a = "))
    b=float(input("b = "))
    return(round(a*b,2))
def cir():
    r=float(input("r = "))
    return(round(math.pi * r ** 2,2))
def tri():
    a=float(input("a = "))
    b=float(input("b = "))
    c=float(input("c = "))
    p=(a + b + c)/2 
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return(round(s,2))
x = input("press 1 to find area for rectangle, 2 for circle and 3 for triangle: ")
if x=='1':
    print(rec())
elif x=='2':
    print(cir())
elif x=='3':
    print(tri())
#task1.2
print()
a = [1,2,3,4,5,8]
b=[5,4,8,7,9,5]
c = [10,5,1,65]
def findSumAndMean(arr):
    summ=0
    mean=0
    print("Original array is: ", arr)
    for i in range (len(arr)):
        summ+=arr[i]
        i+=1
    mean = round(summ/len(arr),2)
    print("sum of the array is ", summ, " and mean is ", mean)
findSumAndMean(a)
findSumAndMean(b)
findSumAndMean(c)
#task2.1
print()
a = float(input("enter the side area of hexagon: "))
def hex_area(a):
    return (3*math.sqrt(3)*(a**2))/2
print("area of hexagon: ",round(hex_area(a),2))
#task2.2
print()
for i in range(3):
    print("enter the sides of the ", i+1," rectangle")
    print("area is ",rec())
#task3.1
print()
def hypo():
    a = int(input("enter the first side: "))
    b = int(input("enter the second side: "))
    return (math.sqrt((a**2)+(b**2)))
print("first triangle: ")
c1 = round(hypo(),2)
print("second triangle: ")
c2 = round(hypo(),2)
if c1>c2:
    print("Hypotenuse for first triangle is greater")
elif c1<c2:
    print("Hypotenuse for second triangle is greater")
else:
    print("Hypotenuses are equal")
#task3.2
print()
string = str(input("Enter the string: ")).lower()
print(" ".join(sorted(string)))
#task4.1
print()
#task5.2
print()
def printDiv(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1
n = int(input("Enter the number to find divisors to: "))
printDiv(n)

#task10.2
print()
str = "Their speech impressed us very much."
print("Original string is: ", str)
print("Reversed string is: "," ".join(list(reversed(str.split()))))
#task15.1
print()
def checkPalindrome(string):
   
    rev = string[::-1]
    if(string == rev):
        return True
    else:
        return False
n = int(input("Enter the n: "))
a = []
a=list(range(0,n+1))
print("The palindromes of their binary notions are: ")
print(a)
for i in range(n+1):
    a[i]=bin(i).replace("0b", "")
    i+=1
a = list(map(str, a))
for i in range(n+1):
    if(checkPalindrome(a[i])):
        print(a[i]," ")
        i+=1
    else:
        i+=1

