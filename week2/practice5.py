import re
#task1
text = "Когда человек сознательно или интуитивно выбирает себе в жизни какую-то цель, жизненную задачу, он невольно дает себе оценку. По тому, ради чего человек живет, можно судить и о его самооценке - низкой ель или высокой."
print("The text is : " + str(text))
count = 0
txt = text.split()
for i in range(len(txt)):
    x = re.findall("^е",txt[i])
    if x:
        count+=1
print(count)
#task2
#txt replace potom find that how you count
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
text="tHiS Is tExT."
print(text)
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
