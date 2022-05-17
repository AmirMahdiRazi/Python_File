str1=input()
data3=[]
data1=str1.split('.')
for i in range(len(data1)):
    data2=data1[i].split(' ')
    data3+=[data2]
b1=True
for i in range(len(data3)):
    for j in range(len(data3[i])):
        if len(data3[i][j]) == 0:
            data3[i].remove('')
            break
for i in range(len(data3)):
    for j in range(len(data3[i])):
            if data3[i][j]==',':
                data3[i].remove(',')
                break
up=[]
len_word=0
for i in range(len(data3)):
    
    for j in range(1,len(data3[i])):
        if i==0:
            if data3[i][j].istitle():
                up+=[j+1,data3[i][j]]
        else:
            if data3[i][j].istitle():
                up+=[len_word+j+1,data3[i][j]]
    len_word +=len(data3[i])    

if(len(up)!=0):
    for i in range(0,len(up),2):
        print(up[i] ,end="")
        print(":" ,end="")
        if up[i+1][len(up[i+1])-1] ==',':
            for j in range(len(up[i+1])-1):
                print(up[i+1][j], end="")
            print()
        else:
            print(up[i+1])
else:
    print('None')