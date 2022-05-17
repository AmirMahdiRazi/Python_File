class test:
    def __init__(self):
        self.name = "Ali"
        self.age = 12
    @property
    def name1(self):
        return "{}-{}".format(self.name,self.age)
    def fullname(self):
        return self.name ,self.age
    @fullname.setter
    def fullname(self):
        return self.name ,self.age
    

t1 = test()
t1.fullname = "ali"
print(t1.fullname())