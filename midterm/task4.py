print()
def sweetest_icecream(string,n):
    aroma = ["plain","vanilla","chocolatechip","strawberry","chocolate"]
    pre=[0,5,5,10,10]
    for i in range (5):
        if(string==aroma[i]):
            return (int(pre[i])+int(n))
        else:
            i+=1
string = str(input("Enter aromatizator: "))
string=string.lower()
n = int(input("Enter kolichestvo posipok: "))
print("Degree of sweetness is: ",sweetest_icecream(string,n))
