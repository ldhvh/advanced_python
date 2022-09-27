print()
arr = str(input("Enter 5 cards with spaces between them: "))
arr = arr.split()
def is_full_house(arr):
    c = []
    for i in range(5):
        c.append(arr.count(arr[i]))
        i+=1
    if (3 in c) and (2 in c):
        return True
    else:
        return False
print(is_full_house(arr))
