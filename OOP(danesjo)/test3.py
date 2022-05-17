class A:
    def func(self):
        print("its A")

class B(A):
    pass
                
class D(B,A):
    pass

cla=D()
print(D.__mro__)
        