class test:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constarctor")
    def print_hello(self, name):
        print("Hello {}".format(name))
class child (test):
    def __init__(self, name, age):
        super().__init__(name, age)
    def print_hello(self, name , age):
        print("HELLO {} {}".format(name , age))
class school:
    def func1(self):
        print("its school")
class chaild1 (school):
    def func2(self):
        print("its child1")
class chaild2 (school):
    def func3(self):
        print("its child2")
class chaild3 (chaild2, chaild1):
    def __init__(self):
        pass
    def func4(self):
        print("its child 3")
        super().func2()
c1 = chaild3()
c1.func4()
#print(help(chaild3))

"""c1 = child("ali",42)
c2 = child("reza",23)
c3 = child("amir",25)
c1.print_hello("ali",53)
c1.print_hello("ali" , 47)"""
"""li=[]
li.append(c1)
li.append(c2)
li.append(c3)
num = None
if num is None :
    li.remove(c1)
print(li[0].name)"""