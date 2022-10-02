#task1
class Rectangle:
    def __init__(self, color="green",width=100,height=100,side=5):
        self.color=color
        self.width=width
        self.height=height
        self.side=side
    def annul_side(self):
        self.width=0
        self.height=0
    def square(self):
        return self.width*self.height
rect1=Rectangle()
print(rect1.color)
print(rect1.square())
rect1=Rectangle("yellow",23,24)
print(rect1.color)
print(rect1.square())
rect1=Rectangle("blue", 10,15)
print(rect1.square())
rect1.annul_side()
print(rect1.square())
#task2
class Name:
    def __init__(self, fname,lname):
        self.fname=fname.lower().title()
        self.lname=lname.lower().title()
        self.full_name=self.fname+" "+self.lname
        self.initials=fname[0].upper()+"."+lname[0].upper()+"."
name1= Name("lEila","zHuRuntaYevA")
print(name1.fname)
print(name1.lname)
print(name1.full_name)
print(name1.initials)
#task3
class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print (self.n1+self.n2)
    def substract(self):
        print(self.n1-self.n2)
    def multiply(self):
        print(self.n1*self.n2)
    def divide(self):
        print(round(self.n1/self.n2,2))
calculator = Calculator(10,5)
calculator.add()
calculator.substract()
