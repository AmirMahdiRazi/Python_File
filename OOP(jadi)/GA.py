
from math import tan
import random
from typing import Counter, NewType
bar=0
def bar_zarbDR(li,i,j):
    global bar
    for k in range(1,8):
        if (i+k == 8 or j+k == 8):
            break
        if li[i+k][j+k]==True:
            bar+=1
        #zar_DR
    for k in range(1,8):
        if (i-k == -1 or j+k == 8):
            break
        if li[i-k][j+k]==True:
            bar+=1
        #zar_DL
    for k in range(1,8):
        if (i+k == 8 or j-k == -1):
            break
        if li[i+k][j-k]==True:
            bar+=1
        #zar_UR
    for k in range(1,8):
        if (i-k == -1 or j-k == -1):
            break
        if li[i-k][j-k]==True:
            bar+=1
        #zar_UL
    for k in range(1,8):
        if j+k==8:
            break
        if li[i][j+k]==True:
            bar+=1
    for k in range(1,8):
        if j-k==-1:
            break
        if li[i][j-k]==True:
            bar+=1
                    
    #ofoghi
    return bar

def mat(li):
    li1=[]
    global bar    
    for i in range(8):
        li0=[]
        for j in range(8):
            li0+=[False]
        li1+=[li0]
    for i in range(8):
        li1[li[i]][i]=True
    #print(li1)
    return li1    

def korom():
    li1=[]
    for i in range(6):
        liran=[0,1,2,3,4,5,6,7]
        if 1:
            li0=[]
            j=0
            x=0
            while j < 8:
                x=random.randrange(0,8)
                li0+=[liran[x]]
                j+=1
        li1+=[li0]
    return li1

def fitness(li0):
    global bar
    bar=0
    li1=[]
    li1=mat(li0)
    barkhord0=0
    barkhord1=0
    for i in range(8):
        barkhord0=bar_zarbDR(li1,li0[i],i)
    barkhord1=barkhord0
    return barkhord1
    
def cross(li0,li1):
    li2=[]
    litmpe1=[]
    litemp2=[]
    litemp3=[]
    litemp4=[]
    lif1=[]
    lif2=[]
    x=random.randrange(0,8)
    litmpe1=li0[0:x]
    litemp4=li0[x:len(li0)]
    litemp2=li1[x:len(li1)]
    litemp3=li1[0:x]
    lif1+=litmpe1
    lif1+=litemp2
    lif2+=litemp3
    lif2+=litemp4
    #print(li0,li1)
    #print(lif1,lif2)
    li2+=[lif1]
    li2+=[lif2]
    return li2

    
def mute(li):
    li1=[]
    for j in range(len(li)):
        li1+=[li[j]]
    x=random.randrange(0,8)
    li1[x]=random.randrange(0,8)
    return li1
################   main   ###########################
likorm=korom()
kol=0
for i in range(6):
    x=fitness(likorm[i])
    likorm[i]+=[40-x]
    kol+=40-x
   
b1=True
x=0
mohem=[0,0,0]
indexmehem=[0,0,0]
c=0
for i in range(6):
        likorm[i]+=[int(likorm[i][8]/kol*1000)]



while (b1):
    kol=0
    for i in range(len(likorm)):
        kol+=likorm[i][8]
    c+=1
    mohem=[0,0,0,0]
    indexmehem=[0,0,0,0]
    x=0
    for i in range(6):
        if likorm[i][8] == 0:
            print(likorm[i])
            b1 =False
    if (c==10):
        #print(likorm)
        break   
    for i in range(6):
        if(likorm[i][8] > mohem[0] or likorm[i][8] > mohem[1] or likorm[i][8] > mohem[2] or likorm[i][8]>mohem[3]):
            if (likorm[i][8] > mohem[0]):
                mohem[0]=likorm[i][8]
                indexmehem[0]=i
            elif(likorm[i][8] > mohem[1]):
                mohem[1]=likorm[i][8]
                indexmehem[1]=i
            elif(likorm[i][8] > mohem[2]):
                mohem[2]=likorm[i][8]
                indexmehem[2]=i
            else:
                mohem[3]=likorm[i][8]
                indexmehem[3]=i
    if (1):
        print(likorm)
        pass
    old=[]
    for i in range(3):
        old+=[likorm[indexmehem[i]][0:8]]
    #cross
    new=[]
    for i in range(3):
        x=random.randrange(0,10)
        if (x!=5 or x!=8):
            y=random.randrange(0,3)
            k=random.randrange(0,3)
            new+=cross(old[k],old[y])
    #muta
    #print(new)
    new1=[]
    for i in range(len(new)):
        x=random.randrange(0,10)
        if(x==3 or x==7 or x==9):  
            #print(new1)
            new1+=[mute(new[i])]
    for i in range(len(new)):
        x=fitness(new[i])
        new[i]+=[40-x]
        kol+=40-x
    for i in range(len(new1)):
        x=fitness(new1[i])
        new1[i]+=[40-x]
        kol+=40-x    
    for i in range(len(new)):
        new[i]+=[0]
        new[i][9]=int((new[i][8]/kol)*1000)
    for i in range(len(new1)):
        new1[i]+=[0]
        new1[i][9]=int((new1[i][8]/kol)*1000)
    #print(new1,new)
    #print(likorm)
    likorm+=new
    #print(new)
    likorm+=new1
    #print(new1)
    mohem=[0,0]
    indexmohem=[0,0]
    bad=[100,100]
    indexbad=[0,0]
    #print(likorm)
    
    for i in range(len(likorm)):
        if(likorm[i][8] > mohem[0] or likorm[i][8] > mohem[1] ):
            if (likorm[i][8] > mohem[0]):
                mohem[0]=likorm[i][8]
                indexmohem[0]=i
            else:
                mohem[1]=likorm[i][8]
                indexmohem[1]=i
            #find mohem
            if (likorm[i][8] < bad[0] or likorm[i][8] < bad[1]):
                if (likorm[i][8] <= bad[0]):
                    bad[0]=likorm[i][8]
                    indexbad[0]=i
                else:
                    bad[1]=likorm[i][8]
                    indexbad[1]=i
            #find bad
    x=random.randrange(0,8)
    y=random.randrange(0,8)
    
    likorm_new=[]
    likorm_new+=[likorm[indexmehem[0]]]
    likorm_new+=[likorm[indexmehem[1]]]
    likorm_new+=[likorm[indexbad[0]]]
    likorm_new+=[likorm[indexbad[1]]]
    likorm_new+=[likorm[x]]
    likorm_new+=[likorm[y]]
    
    likorm=[]
    likorm+=likorm_new