class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def nameeq(self):
        if self.name == "alo":
            print("no name")


for i in range(0,10,2):    
    name=input("enter name : ")
    ali=person(name,40)
    ali.nameeq()
    print(i)
