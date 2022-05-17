
inpu0=["S-I","P-I","M-I","P-S","M-S","M-P"]

inpu1=[]
inpu=[]
#Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Spain=["Spain",0,0,0,0,0]
Iran=["Iran",0,0,0,0,0]
Portugal=["Portugal",0,0,0,0,0]
Morocco=["Morocco",0,0,0,0,0]
#Spain=S ,Iran=I ,Portugal=P ,Morocco=M
for i in range (1):
    inpu1.append(input())

for j in range (1):
    inpu=[]
    inpu.append(int(inpu1[j][0]))
    inpu.append(int(inpu1[j][2]))
    if (inpu0[j][0]=='S' and inpu0[j][2]=='I') or (inpu0[j][0]=='I' and inpu0[j][2]=='S'):
        if inpu0[j][0]=='S' and inpu0[j][2]=='I':
            if inpu[0]>inpu[1]:
                Spain[1]+=1
                Spain[5]+=3
                Spain[4]+=inpu[0]
                Iran[4]-=inpu[0]
            elif inpu[0]<inpu[1]:
                Iran[1]+=1
                Iran[5]+=3
                Iran[4]+=inpu[0]
                Spain[4]-=inpu[1]
            else:
                spain[2]+=1
                Iran[2]+=1
                Spain[5]+=1
                Iran[5]+=1

        if inpu0[j][0]=='I' and inpu0[j][2]=='S':
            if inpu[0]>inpu[1]:
                Iran[1]+=1
                Iran[5]+=3
                Iran[4]+=inpu[0]
                Spain[4]-=inpu[0]
            elif inpu[0]<inpu[1]:
                Spain[1]+=1
                Spain[5]+=3
                Spain[4]+=inpu[0]
                Iran[4]-=inpu[0]
            else:
                spain[2]+=1
                Iran[2]+=1
                Spain[5]+=1
                Iran[5]+=1

#-------------------------------------------------------------dasdasds
    if (inpu0[j][0]=='P' and inpu0[j][2]=='I') or (inpu0[j][0]=='I' and inpu0[j][2]=='P'):
        if inpu0[j][0]=='P' and inpu0[j][2]=='I':
            if inpu[0]>inpu[1]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[0]
                Iran[4]-=inpu[0]
            elif inpu[0]<inpu[1]:
                Iran[1]+=1
                Iran[5]+=3
                Iran[4]+=inpu[0]
                Portugal[4]-=inpu[0]
            else:
                Portugal[2]+=1
                Iran[2]+=1
                Portugal[5]+=1
                Iran[5]+=1
                
        if inpu0[j][0]=='I' and inpu0[j][2]=='P':
            if inpu[0]>inpu[1]:
                Iran[1]+=1
                Iran[5]+=3
                Iran[4]+=inpu[0]
                Portugal[4]-=inpu[0]
            elif inpu[0]<inpu[2]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[0]
                Iran[4]-=inpu[0]
            else:
                Portugal[2]+=1
                Iran[2]+=1
                Portugal[5]+=1
                Iran[5]+=1 
#---------------------------Mra




if (inpu0[j][0]=='M' and inpu0[j][2]=='I') or (inpu0[j][0]=='I' and inpu0[j][2]=='M'):
        if inpu0[j][0]=='M' and inpu0[j][2]=='I':
            if inpu[j][0]>inpu[j][2]:
                Morocco[1]+=1
                Morocco[5]+=3
                Morocco[4]+=inpu[j][0]
                Iran[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Iran[1]+=1
                Iran[5]+=3
                Iran[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            else:
                Morocco[2]+=1
                Iran[2]+=1
                Morocco[5]+=1
                Iran[5]+=1

        if inpu0[j][0]=='I' and inpu0[j][2]=='M':
            if inpu[j][0]>inpu[j][2]:
                Iran[1]+=1
                Iran[5]+=3
                Iran[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Morocco[1]+=1
                Morocco[5]+=3
                Morocco[4]+=inpu[j][0]
                Iran[4]-=inpu[j][0]
            else:
                Morocco[2]+=1
                Iran[2]+=1
                Morocco[5]+=1
                Iran[5]+=1

#-----------
if (inpu0[j][0]=='S' and inpu0[j][2]=='P') or (inpu0[j][0]=='P' and inpu0[j][2]=='S'):
        if inpu0[j][0]=='S' and inpu0[j][2]=='P':
            if inpu[j][0]>inpu[j][2]:
                Spain[1]+=1
                Spain[5]+=3
                Spain[4]+=inpu0[j][0]
                Portugal[4]-=inpu0[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[j][0]
                Spain[4]-=inpu[j][0]
            else:
                Spain[2]+=1
                Portugal[2]+=1
                Spain[5]+=1
                Portugal[5]+=1

        if inpu0[j][0]=='P' and inpu0[j][2]=='S':
            if inpu[j][0]>inpu[j][2]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[j][0]
                Spain[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Spain[1]+=1
                Spain[5]+=3
                Spain[4]+=inpu[j][0]
                Portugal[4]-=inpu[j][0]
            else:
                Spain[2]+=1
                Portugal[2]+=1
                Spain[5]+=1
                Portugal[5]+=1
#--------------------------------------------------------------

if (inpu0[j][0]=='M' and inpu0[j][2]=='S') or (inpu0[j][0]=='S' and inpu0[j][2]=='M'):
        if inpu0[j][0]=='M' and inpu0[j][2]=='S':
            if inpu[j][0]>inpu[j][2]:
                Morocco[1]+=1
                Morocco[5]+=3
                Morocco[4]+=inpu[j][0]
                Spain[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Spain[1]+=1
                Spain[5]+=3
                Spain[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            else:
                Morocco[2]+=1
                Spain[2]+=1
                Morocco[5]+=1
                Spain[5]+=1

        if inpu0[j][0]=='S' and inpu0[j][2]=='M':
            if inpu[j][0]>inpu[j][2]:
                Spain[1]+=1
                Spain[5]+=3
                Spain[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Morocco[1]+=1
                Morocco[5]+=3
                Morocco[4]+=inpu0[j][0]
                Spain[4]-=inpu0[j][0]
            else:
                Morocco[2]+=1
                Spain[2]+=1
                Morocco[5]+=1
                Spain[5]+=1

#--------------------------------------------------------------
if (inpu0[j][0]=='M' and inpu0[j][2]=='P') or (inpu0[j][0]=='P' and inpu0[j][2]=='M'):
        if inpu0[j][0]=='M' and inpu0[j][2]=='P':
            if inpu[j][0]>inpu[j][2]:
                Morocco[1]+=1
                Morocco[5]+=3
                Morocco[4]+=inpu[j][0]
                Portugal[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            else:
                Morocco[2]+=1
                Portugal[2]+=1
                Morocco[5]+=1
                Portugal[5]+=1

        if inpu0[j][0]=='P' and inpu0[j][2]=='M':
            if inpu[j][0]>inpu[j][2]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            elif inpu[j][0]<inpu[j][2]:
                Portugal[1]+=1
                Portugal[5]+=3
                Portugal[4]+=inpu[j][0]
                Morocco[4]-=inpu[j][0]
            else:
                Morocco[2]+=1
                Portugal[2]+=1
                Morocco[5]+=1
                Portugal[5]+=1

