count=int(input())
str1=[]
str2=[]
f=[]
m=[]
name=[]
for i in range(count):
    afrad=input()
    str1+=[afrad]
for i in range(len(str1)):
    str3=str1[i].split('.')
    str3[1]=str3[1].lower()
    str3[1]=str3[1].capitalize()
    name+=[str3[1]]
    str2+=[str3]
#for i in range(len(str2))
for i in range (len(str2)):
    if str2[i][0] =='f':
        f+=[str2[i]]
    else:
        m+=[str2[i]]

name.sort()
for j in range(len(name)):
    for i in range(len(f)):
        if name[j]==f[i][1]:
            print(f[i][0],f[i][1],f[i][2])
for j in range(len(name)):
    for i in range(len(m)):
        if name[j]==m[i][1]:
            print(m[i][0],m[i][1],m[i][2])
