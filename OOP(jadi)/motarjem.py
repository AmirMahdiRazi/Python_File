count=int(input())
str1=[]
out=[]
for i in range(count):
    vorodi=input()
    data1=vorodi.split(' ')
    str1 +=[data1]
vorodi=input()
data2=vorodi.split(' ')
for i in range(len(data2)):
    b1=False
    for j in range(count):
        for k in range(1,4):
            if data2[i]==str1[j][k]:
                out+=[str1[j][0]]
                b1=True
                break
        if j==count-1 and b1==False:
            out+=[data2[i]]
            break
for i in range(len(out)):
    print(out[i],end=" ")