
def result(li1):
    res1=[]
    res2=[]
    res3=[]
    if li1[0] > li1[1]:
        res1=[1,0,0,li1[0]-li1[1],3]
        res2=[0,1,0,li1[1]-li1[0],0]

    elif li1[0] < li1[1]:
        res2=[1,0,0,li1[1]-li1[0],3]
        res1=[0,1,0,li1[0]-li1[1],0]

    elif li1[0] == li1[1]:
        res1=[0,0,1,0,1]
        res2=[0,0,1,0,1]
    res3+=[res1,res2]
    return res3
ir=['i',0,0,0,0,0]
sp=['s',0,0,0,0,0]
po=['p',0,0,0,0,0]
ma=['m',0,0,0,0,0]
match=[['i','s'],['i','p'],['i','m'],['s','p'],['s','m'],['p','m']]
li=[]
team=[]
for i in range(6):
    num=input()
    num2=num.split('-')
    li+=[[int(num2[0]),int(num2[1])]]
#print(li)
for i in range(6):
    team=[]
    team+=result(li[i])
    #print(team)
    #print(li[i])
    #print(match[i])
    if match[i] == ['i','s']:
        for j in range(1,6):
            ir[j]+=team[0][j-1]
            sp[j]+=team[1][j-1]
    elif match[i] == ['i','p']:
        for j in range(1,6):
            ir[j]+=team[0][j-1]
            po[j]+=team[1][j-1]
    elif match[i] == ['i','m']:
        for j in range(1,6):
            ir[j]+=team[0][j-1]
            ma[j]+=team[1][j-1]
    elif match[i] == ['s','p']:
        for j in range(1,6):
            sp[j]+=team[0][j-1]
            po[j]+=team[1][j-1]
    elif match[i] == ['s','m']:
        for j in range(1,6):
            sp[j]+=team[0][j-1]
            ma[j]+=team[1][j-1]
    elif match[i] == ['p','m']:
        for j in range(1,6):
            po[j]+=team[0][j-1]
            ma[j]+=team[1][j-1]
max=[]
li=[]
jadval=[ir,sp,po,ma] 
################################################################################### 

for i in range(4):
    max+=[jadval[i][5]]
max.sort(reverse=True)
for i in range(len(max)):
    x = max.count(max[i])
    li+=[max[i],x]
k=4
out=[]
jadval1=[]
for i in range(len(jadval)):
    jadval1+=[[jadval[i][5],jadval[i][1],jadval[i][0],jadval[i][2],jadval[i][3],jadval[i][4]]] 
jadval1.sort(reverse=True)
count=0
for i in range(4):
    for j in range(i+1,4):
        if jadval[i][1:5]==jadval[j][1:5]:
            count+=1
            i+=1
            break
if (count!=3):
    for i in range(4):
        if i==3:
            break
        elif jadval1[i][0:2]==jadval1[i+1][0:2]:
            if jadval1[i][2]>jadval1[i+1][2]:
                jadval1[i],jadval1[i+1]=jadval1[i+1],jadval1[i]
                break
    for j in range(4):
        out+=[[jadval1[j][2],jadval1[j][1],jadval1[j][3],jadval1[j][4],jadval1[j][5],jadval1[j][0]]]
else:
    jadval.sort()
    out=jadval
str2=['i','m','p','s']
if (count !=3):
    for i in range(4):
        for j in range(4):
            if out[i]==jadval[j]:

                if j==0:
                    print("Iran",end="  ")
                elif j==1 :
                    print("Spain",end="  ")
                elif j==2 :
                    print("Portugal",end="  ")
                elif j==3 : 
                    print("Morocco",end="  ")
                print("wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d" % (out[i][1],out[i][2],out[i][3],out[i][4],out[i][5]))

else:
    for i in range(4):
            if out[i][0]==str2[i]:
                if i==0:
                    print("Iran",end="  ")
                elif i==1 :
                    print("Morocco",end="  ")
                elif i==2 :
                    print("Portugal",end="  ")
                elif i==3 : 
                    print("Spain ",end="  ")
                print("wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d" % (out[i][1],out[i][2],out[i][3],out[i][4],out[i][5]))