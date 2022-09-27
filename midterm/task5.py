print()
def check_sequence(lis):
    a=0
    d=0
    for i in range (len(lis)):
        if(lis[i-1]>lis[i]):
            d+=1
            i+=1
        elif(lis[i-1]<lis[i]):
            a+=1
            i+=1
        else:
            return 0
    if(a==(len(lis)-1)):
        return 1
    elif(d==(len(lis)-1)):
        return -1
    else:
        return 0
lis = input("Enter sequence: ")
lis = lis.split()
print(check_sequence(lis))
