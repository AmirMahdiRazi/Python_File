import random
class Person:
    def __init__(self,name):
        self.name=name

class FB(Person):
    def st(self,nteam):
        self.nteam=nteam
    def info(self):
        print(self.name,self.nteam)

def inp(lis):
    lis=lis.split(" - ")
    return lis

team=[]
num=0
while True:
    team.append("A")
    team.append("B")
    num +=1
    if num==11:
        break


names = input()
names = inp(names)
li = []
counter = 0
count = 21
while True:
    num=random.randint(0,count)
    namein=names[num]
    teamin=team[num]
    names.remove(namein)
    team.remove(teamin)
    temp=FB(namein)
    temp.st(teamin)
    li.append(temp)
    counter +=1
    count -=1
    temp.info()
    if counter==22:
        break
print(li[0])


    