import re
import requests
from bs4 import BeautifulSoup
import mysql.connector
from sklearn import tree

cnx = mysql.connector.connect(user="root",password="Razi0023161469",host="127.0.0.1",database="Car")
crusor=cnx.cursor()



#==========================create table================================#
#qureyCre="""CREATE TABLE cars (
#    CID int,
#    NAMECAR varchar(50),
#    COLORCAR int,
#    KARKARDCAR int,
#    ACCIDENTCAR int,
#    COSTCAR int
#)"""
#crusor.execute(qureyCre)













#==========================================read from DB==================================================#
str1=[]
query='select * from cars'
crusor.execute(query)
for (NAME) in crusor:
    str1.append(NAME)
COLOR_cars=[[0,"Beige"],[1,"Black"],[2,"Blue"],[3,"Brown"] ,[4,"Gray"] ,[5,"Green"] ,[6,"Red"] ,[7,"Silver"] ,[8,"White"],[9,"Orange"],[10,"Purple"],[11,"Yellow"],[12,"Unknown"]]
str3_COLOR=[]
str4_COLOR=[]
i=0
def selectcolor(color):
    global COLOR_cars
    for i in range(len(COLOR_cars)):
        if color == COLOR_cars[i][1]:
            return COLOR_cars[i][0]
    return 12

def dec_color(num):
    global COLOR_cars
    for i in range(len(COLOR_cars)):
        if num == COLOR_cars[i][0]:
            return COLOR_cars[i][1]
    return "Unknown"









######################===================save in DB===================############################

number=1
j=[]
while(number <20 ):
    if (number == 1):
        print("Start to Read Page Pls Wait")
    r = requests.get("https://www.truecar.com/used-cars-for-sale/listings/?page=%d" % number)
    soup=BeautifulSoup(r.text,"html.parser")
    li_desc=[]
    li_name=[]
    li_gheimat=[]
    li_color=[]
    li_accident=[]
    number+=1
    
    str1=[]
    query='select * from cars'
    crusor.execute(query)
    for (NAME) in crusor:
        str1.append(NAME)

    
    name_car = soup.find_all('span',attrs={'class' : 'vehicle-header-make-model text-truncate'})

    karkard_car = soup.find_all('div',attrs={'data-test' : 'vehicleMileage'})

    gheimat_car=soup.find_all('div',attrs={'class' :'padding-left-3 vehicle-card-bottom-pricing-secondary vehicle-card-bottom-max-50'})

    color_car =soup.find_all('div',attrs={'class' :'vehicle-card-location font-size-1 margin-top-1 text-truncate'})
    
    accident_car = soup.find_all('div',attrs={'data-test' :'vehicleCardCondition'})

    for name in name_car:
        result1=re.sub(r'\s+',' ',name.text).strip()
        li_name.append(result1)

    for karkard in karkard_car:
        result1=re.findall(r'\d+',karkard.text)
        karka=''.join(result1)
        li_desc.append(int(karka))

    for ghaimat in gheimat_car:
        result1=re.findall(r'\d+',ghaimat.text)
        ghe=''.join(result1)
        li_gheimat.append(int(ghe))
    
    for color in color_car:
        result1=re.findall(r'\w+',color.text)
        c1=selectcolor(result1[0])
        li_color.append(c1)
    
    for accident in accident_car:
        result1=re.findall(r'^\w+',accident.text)
        if result1[0] == 'No':
            li_accident.append(0)
        else :
            li_accident.append(int(result1[0]))

    print(li_desc)
    range1=len(str1)+len(li_name)
    len_str1=(len(str1))  
    if len(str1) ==0:
        for i in range(len_str1,range1):
            
            str2=[]
            str2+=[i,li_name[i-len_str1],li_color[i-len_str1],li_desc[i-len_str1],li_accident[i-len_str1],li_gheimat[i-len_str1]]
            #print(str2[0],str2[1],str2[2],str2[3],str2[4],str2[5])
            crusor.execute('insert into cars values (%i,\'%s\',\'%i\',%i,%i,%i)' % (str2[0],str2[1],str2[2],str2[3],str2[4],str2[5]))
    else :
        for i in range(len_str1,range1):
            flag=False
            str2=[]
            str2+=[i,li_name[i-len_str1],li_color[i-len_str1],li_desc[i-len_str1],li_accident[i-len_str1],li_gheimat[i-len_str1]]
            for j in range(len_str1):
                if str2[1] == str1[j][1] and str2[2] == str1[j][2] and str2[3] == str1[j][3] and str2[4] == str1[j][4] and str2[5] == str1[j][5]:
                    flag=True
                    break
            if flag == False:
                #print(str2)
                crusor.execute('insert into cars values (%i,\'%s\',\'%i\',%i,%i,%i)' % (str2[0],str2[1],str2[2],str2[3],str2[4],str2[5]))
    if (number % 5) ==0:
        print("Read Page %d ,remain %d Pls wait" % (number,20-number))
#######################============================Name carbar cars====================#

str3_NAME=[]
query='SELECT DISTINCT NAMECAR FROM cars;'
crusor.execute(query)
for (NAME) in crusor:
    str3_NAME.append(NAME)


max_name=0
for i in range(len(str3_NAME)):
    if len(str3_NAME[i][0]) >= max_name:
        max_name=len(str3_NAME[i][0])  

i=0
while(i<len(str3_NAME)):
    if (len(str3_NAME)-i) < 8 :
        for j in range(len(str3_NAME)-i):
            x = str3_NAME[i+j][0].center(max_name)
            print(x,end='||')
        print()   
        break    
    for j in range(8):
        x = str3_NAME[i+j][0].center(max_name)
        print(x,end='||')
    print()
        
    
    i+=8

name_car_carbalr=input("Enter Name Car :")


i=0
while(i<len(COLOR_cars)):
    x = COLOR_cars[i][1].center(10)
    print(x,end='||')
    i+=1

print()
color_carbalr=input("Enter Color Car :")
name_color_carbar=selectcolor(color_carbalr)

name_accident_carbalr=int(input("Enter Name Car (If have Accident Enter count ,else Enter 0 ) :"))
name_karkard_carbalr=int(input("Enter Mileage Car (mi) :"))

str1=[]
x=[]
y=[]
query="select * from cars where namecar = %s"
adr=(name_car_carbalr,)
i=0

crusor.execute(query,adr)
for (NAME) in crusor:
    k=[]
    str1.append(NAME)
    x +=[[str1[i][2],str1[i][3],str1[i][4]]]
    y +=[str1[i][5]]
    i+=1

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

new_data=[[name_color_carbar,name_accident_carbalr,name_karkard_carbalr]]  
answer= clf.predict(new_data)
print("Price your car :",answer[0])

for i in range (10):
    print("/\\" , end="")
print()
for i in range (10):
    print("||" , end="")
print()

for i in range (len(x)):
    for j in range(6):
        if j==2:
            color=dec_color(str1[i][j])
            print(color,end=" ")
        else:
            print(str1[i][j],end=" ")
    print()
    

cnx.commit()

cnx.close()