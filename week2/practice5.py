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
#task4
def count(w, c) :
    res = 0
    for i in range(len(w)) :
        if (w[i] == c):
            res = res + 1
            return res
str="Forty moderate far into. Newspaper blush points answer. Suitable luckily poor."
c='a'
print(count(str, c))
#task5
print()
text="tHiS Is tExT."
print("Original text -> ",text)
text.lower()
print(text)
#task8
print(len(s.split))
#task9

w=str.split()
list=[]
for word in w:
    if w== 'beach':
        list1.append(word)


lengthstring= len(list1)

print("The number of times the word beach occurs in the string is ", lengthstring)
