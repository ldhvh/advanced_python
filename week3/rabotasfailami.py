f = open("test.txt","r")
print("file.closed: "+str(f.closed))
print("file.mode: "+f.mode)
print("file.name: "+f.name)
f.close()
#reading
f = open("test.txt","r")
print(f.readline())
f.close()
#writing
f = open("test.txt","a")
f.write("added string")
f.close()
f = open("test.txt","r")
print(f.read())
#additional
line = {}
res={}
with open("test.txt","r") as f:
    for i in range(10):
        line[i]=f.readline()
        stroka=line[i].split(' ')
        a=int(stroka[0])
        b=int(stroka[1])
        res[i]=(a+b)/2
with open("test2.txt","a") as result:
    for i in range(10):
        res[i]=str(res[i])
        result.write(res[i]+"\n")
