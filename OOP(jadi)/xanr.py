def func(li):
    li=li.split(" ")
    return li


strx=["Action","Adventure","Comedy", "History","Horror","Romance"]
count=[0,0,0,0,0,0]
num1=int(input())
str1=[]
str2=[]
for i in range(num1):
    str3=input()
    str1.append(str3)

for i in range(num1):
    str2=func(str1[i])
    for j in range(1,4):
        for k in range(0,6):
            if str2[j]==strx[k]:
                count[k] +=1
i=0

while i<6:
    j=0
    bo=False
    num2=count[i]
    strx1=strx[i]
    num4=count[i]
    while j+i <6:
        if num2<count[j+i]:
            num2=count[j+i]
            strx2=strx[j+i]
            num3=j+i
            bo=True
        j +=1
    if bo:
        count[i],count[num3]=num2,num4
        strx[i],strx[num3]= strx2,strx1
    i +=1      

for number in range(6):
    print (strx[number], ":",count[number])