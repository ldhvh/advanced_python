import math
import sys
print()
#task1.1
arr=[[0,0,0],[0,0,0],[0,0,0]]
d=0
print("Enter the elements of the array:")
for i in range(3):
    for j in range(3):
        arr[i][j] = int(input())
     if i>j:
             d+=arr[i][j]
print("The sum of below diagonal elements is:",bd)
#task1.2
print()
m=100
def sR(ms, n, m):
    print("{", end = "")
    for i in range(n):
        minm = ms[i][0]
        for j in range(1, m, 1):
            if (ms[i][j] < minm):
                minm = ms[i][j]
        print(minm, end = ",")
    print("}")
def sC(ms, n, m):
    print("{", end = "")
    for i in range(m):
        minm = ms[0][i]
        for j in range(1, n, 1):
            if (ms[j][i] < minm):
                minm = ms[j][i]
        print(minm, end = ",")
 
    print("}")
if __name__ == '__main__':
    n = 3
    m = 3
    ms = [[5, 7, 6],
           [2, 9, 1 ],
           [ 4, 5, 7 ]];
    print("Minimum element of row is",
                                 end = " ")
    sR(ms, n, m)
    print("Minimum element of column is",
                                    end = " ")
    sC(ms, n, m)
#task2.1
print()
def isMagicSquare(cub) :
  n = len(cub)
  sumd1=0
  sumd2=0
  for i in range(n):
    sumd1+=cub[i][i]
    sumd2+=cub[i][n-i-1]
  if not(sumd1==sumd2):
    return False
  for i in range(n):
    sumr=0
    sumc=0
    for j in range(n):
      sumr+=cub[i][j]
      sumc+=cub[j][i]
    if not(sumr==sumc==sumd1):
      return False
  return True
cub = [[5, 7, 6],
        [2, 9, 1 ],
        [ 4, 5, 7 ]];
     
if (isMagicSquare(mat)) :
    print( "is Magic Square")
else :
    print( "not a magic Square")
#task2.2
print()
def interchangeFirstLast(cub, n, m):
    for i in range(n):
        t = cub[i][0]
        cub[i][0] = mat[i][n-1]
        cub[i][n-1] = t
if __name__ == "__main__":
    cub = [[5, 7, 6],
        [2, 9, 1 ],
        [ 4, 5, 7 ]];
    n = 4
    m = 4
    interchangeFirstLast(cub, n, m)
    for i in range(n):
        for j in range(m):
            print(cub[i][j], end=" ")
        print("\n")
#task3.1
print()
def transpose(cub, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = cub[j][i]
def isSymmetric(cub, N):
    tr = [ [0 for j in range(len(cub[0])) ] for i in range(len(mat)) ]
    transpose(cub, tr, N)
    for i in range(N):
        for j in range(N):
            if (cub[i][j] != tr[i][j]):
                return False
    return True
cub = [[5, 7, 6],
        [2, 9, 1 ],
        [ 4, 5, 7 ]];
if (isSymmetric(cub, 3)):
    print "true"
else:
    print "false"
#task3.2

print()
N = 3
M = 7
def rearrangge(a, b, cub) :
    for i in range(N) :
        for j in range(M) :
            if (cub[i][j] == 1) :
                print(min(a[i], b[j]), end = " ");
            else :
                print(0, end = " ");
        print()
if __name__ == "__main__" :
 
    a = [4, 2, 3]
    b = [3, 1, 0, 0, 4, 0, 5]
     
    cub = [
   [1, 0, 0, 0, 1, 0, 1],
   [0, 0, 1, 0, 0, 1, 1],
   [1, 1, 0, 1, 1, 0, 0]]
             
    rearrangge(a, b, cub);
#task4.1
print()
def findMax(cub):
    idx = -1
    maxSum = -sys.maxsize
    for i in range(0, N):
        sum = 0
        for j in range(0, N):
            sum += cub[i][j]
        if (sum > maxSum):
            maxSum = sum
            idx = i
    res = [idx, maxSum]
    return res
cub = [[5, 7, 6],
        [2, 9, 1 ],
        [ 4, 5, 7 ]];
ans = findMax(cub)
print("Row", ans[0] + 1, "has max sum", ans[1])
#task4.2
print()
import numpy
x = numpy.array([[3, 7], [5, 8]])
y = numpy.array([[10, 1], [3, 2]])
print ("The multiplication of matrix is : ")
print (numpy.multiply(x,y))
print ("The product of matrices is : ")
print (numpy.dot(x,y))
