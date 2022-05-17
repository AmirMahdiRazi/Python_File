import mysql.connector
str1=[]
num=0
num1=[]
num2=[]
index=[]
b1=False
cnx = mysql.connector.connect(user="root",password="Razi0023161469",host="127.0.0.1",database="work")


crusor=cnx.cursor()

query='select * from people'
crusor.execute(query)

for (name , Weight, Height ) in crusor:
    str1.append(name)
    str1.append(Weight)
    str1.append(Height)
    
#-------------------------------
temp=[]
temp2=[]
for i in range(2,12,3):
    temp.append(str1[i])
    temp2.append(str1[i-1])


age = []
for i in temp:
    age += [int(i)]

name =temp2

n = len(age)
i = 0

while i < n:

    #          ### FIND MIN ###
    min = age[i]
    index = i
    for j in range(i, n):
        if age[j] > min:
            min = age[j]
            index = j

    #          ### FIND DUPLICATES

    li = []
    idx = []
    for f in range(n):
        if age[f] == min:
            li += [name[f]]
            idx += [f]

    #            ### SWAP ###

    if len(li) == 1:
        temp_age = age[index]
        temp_name = name[index]
        age[index] = age[i]
        name[index] = name[i]
        age[i] = temp_age
        name[i] = temp_name
        i += 1
    else:
        li.sort()
        for k in range(len(li)):
            temp_age = age[idx[k]]
            age[idx[k]] = age[i+k]
            name[idx[k]] = name[i+k]
            age[i+k] = temp_age
            name[i+k] = li[k]
        i += len(li)
for j in range(n):
    for i in range(2,12,3):
          if str1[i-1]==name[j] and str1[i]==age[j]:
              print (str1[i-2],str1[i],str1[i-1])


    

 
cnx.close()