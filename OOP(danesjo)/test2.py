class A:
    def func(self):
        print("its A")
        
class B:
    def func(self):
        print("its B")

class C (A, B):
    def func(self):
        print("its C")

class D:
    def func(self):
        print("its D")
        

class F (C ,D):
    def func(self):
        print("its F")

clas = F()

print(F.__mro__)