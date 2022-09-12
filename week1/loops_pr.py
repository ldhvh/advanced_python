#ex1
price=int(input("The price for 1kg of sweets: "))
x=0
n=10
for i in range(n):
    i+=1
    x+=price
    print("Price of ",str(i),"kg sweets is",str(x))
#ex2
x=0
t=0
n=int(input("Enter total count of numbers :"))
list = []
for i in range(0, n):
    list.append(int(input()))
      
while (x<len(list)):
    t+=list[x]
    x+=1
print("Number of all elements in sequence is ", len(list))
print("Sum of all elements in the sequence is ", t)
