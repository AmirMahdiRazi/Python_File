class A:
    def __init__(self):
        self.a=20
        self._b=30
        self.__c=30
    def __print_C(self):
        print(self.__c)
    def print_P(self):
        self.__print_C()    
class B(A):
    """def __init__(self):
        super().__init__()"""
    

B1=B()
A1=A()
print(A1.print_P())
print(dir(A1))