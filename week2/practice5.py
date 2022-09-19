import re
#task1
text = "Когда ЕЛЬ человек сознательно или интуитивно выбирает себе в жизни какую-то цель, жизненную задачу, он невольно дает себе оценку. По тому, ради чего человек живет, можно судить и о ЕГО самооценке - низкой ЕЛЬ или высокой."
print("The text is : " + str(text))
count = 0
txt = text.split()
for i in range(len(txt)):
    x = re.findall("^е",txt[i])
    if x:
        count+=1
print(count)

#task2
print()
text="You know what to do: practice. You may be required to bring many things: sleeping bags, pans, utensils, and warm clothing. I want the following items: butter, sugar, and flour."
print("Original text is as follows -> ",text)
print("Replaced text -> ",text.replace(':','%'))
print("The number of replacements is ", text.count(':'))

#task3
print()
print("Text without dots is -> ",text.replace('.',''))
print("Number of characters removed is ",text.count('.'))

#task4?????????????????????????????????????????????
print()
def count(w, c) :
    res = 0
    for i in range(len(w)) :
        if (w[i] == c):
            res = res + 1
            return res
str="Forty moderate far into. Newspaper blush points answer. Suitable luckily poor."
print(str)
c='a'
print(count(str, c))

#task5
print()
text="tHiS Is tExT."
print("Original text -> ",text)
text.lower()
print(text)

#task6
print()
print("Original text is -> ", str)
print("Text without As is -> ",str.replace('a',''))
print("Number of characters removed is ",str.count('a'))

#task7
print()
line = list(str)
print("Original text is -> ", str)
for i in range(round(len(line)/2)):
    if line[i]=='n' or line[i]=='N':
        line[i]='*'
        i+=1
    else:
        i+=1
print("".join(line))

#task8
print()
print("Original text is -> ", str)
print("Number of words in a text is ", len(str.split()))

#task9
print()
print("Original text is -> ", str)
s=str.lower()
w=s.split()
word="answer"
count=0
for i in range (len(w)):
    if w[i]== word or w[i]==word+".":
        count+=1
        i+=1
    else:
        i+=1
print("The number of times the word answer occurs in the string is ", count)

#task10
print()
print("Original text is -> ", str)
line=list(str)
for i in range(len(line)):
    if line[i]==" " and line[i]!=line[len(line)-1]:
        line[i+1]=line[i+1].upper()
        i+=1
    else:
        i+=1
print("".join(line))

#task11
print()
str = "nnnz,cSnndjbfvdzkfvb!! dcjbsc!is nn!!!"
print("Original text is -> ", str)
print("The longest sequence of consecutive n letters is ",len(max(re.compile("(n+n)*").findall(str))))
print("Replaced text -> ",str.replace("!","."))

#task12
print()
def getWords(sentence, letter):
    regex = r'\b(\w*#)\b'.replace('#', letter)
    return re.findall(regex, sentence, re.I)
str = "abacI abaculi abassI acanthi, acanthopterI, acanthopterygiI Week ends in a minute. Lalalala"
result = getWords(str, "I")
print(result)

#task15
print()
print("Original text is -> ", str)
print("Number of ts in text is ",str.count("t"))
