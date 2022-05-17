class Student:
    def __init__(self,total,age,height,weight):
        self.total=total
        self.age=age
        self.hight=height
        self.weight=weight

    def info(self):
        print(self.total,self.age,self.hight,self.weight)

    def avg_age(self):
        return self.age/self.total
    def avg_hight(self):
        return self.hight/self.total
    def avg_weight(self):
        return self.weight/self.total

    
def inp(lis):
    lis=input()
    lis=lis.split(" ")
    lis1=0
    for i in lis:
        lis1=lis1+int(i)
    return lis1

B_age,A_age,A_result,B_result,B_we,A_we,B_he,A_he=[],[],[],[],[],[],[],[]
A_total=int(input())
A_age=inp(A_age)        
A_he=inp(A_he)
A_we=inp(A_we)
B_total=int(input())
B_age=inp(B_age)        
B_he=inp(B_he)
B_we=inp(B_we)
A = Student(A_total,A_age,A_he,A_we)
B = Student(B_total,B_age,B_he,B_we)
A_result.append(A.avg_age())
B_result.append(B.avg_age())
A_result.append(A.avg_hight())
B_result.append(B.avg_hight())
A_result.append(A.avg_weight())
B_result.append(B.avg_weight())

for j in range(3):
    print(A_result[j])

for k in range(3):
    print(B_result[k])

if A_result[1] > B_result[1]:
    print ("A")
elif A_result[1] < B_result[1]:
    print("B")
else:
    
    if A_result[2] > B_result[2]:
        print ("B")
    elif A_result[2] < B_result[2]:
        print("A")
    else:
        print("Same")

