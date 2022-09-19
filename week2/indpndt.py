#task1
li = input("Enter the numeric list ")
li=list(li[::-1])
print("The reverse list is ","".join(li))

#task2
print()
def change(list):
    list[0], list[len(list)-1] = list[len(list)-1], list[0]
    return list
print("List with swapped first and last element: ","".join(change(li)))

#task3
print()
def to_list(*args):
  print([i for i in args])
print("The lists are:")
to_list(10,20,30)
to_list(4,2)
to_list(4,8,3,5,1,9,3)
    
#task4
print()
