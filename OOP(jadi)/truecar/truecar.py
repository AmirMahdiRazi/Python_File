import re
import requests
from bs4 import BeautifulSoup
#import mysql.connector

#cnx = mysql.connector.connect(user="root",password="Razi0023161469",host="127.0.0.1",database="Car1")
#crusor=cnx.cursor()







#qureyCre="""CREATE TABLE cars (
 #   NAME varchar(50),
 #   karkard varchar(50),
 #   gheimat varchar(50)
#)"""
#crusor.execute(qureyCre)








number=1
count=0
order_name=input("Enter Name car :")
while(count <20 ):
    r = requests.get("https://www.truecar.com/used-cars-for-sale/listings/?page=%d&sort[]=best_match" , number)
    soup=BeautifulSoup(r.text,"html.parser")
    li_desc=[]
    li_name=[]
    li_gheimat=[]
    number+=1
    name_car = soup.find_all('span',attrs={'class' : 'vehicle-header-make-model text-truncate'})

    karkard_car = soup.find_all('div',attrs={'data-test' : 'vehicleMileage'})

    gheimat_car=soup.find_all('div',attrs={'class' :'padding-left-3 vehicle-card-bottom-pricing-secondary vehicle-card-bottom-max-50'})
    

    for name in name_car:
        result1=re.sub(r'\s+',' ',name.text).strip()
        li_name.append(result1)

    for name in karkard_car:
        result1=re.sub(r'\s+',' ',name.text).strip()
        li_desc.append(result1)

    for ghaimat in gheimat_car:
        result1=re.sub(r'\s+',' ',ghaimat.text).strip()
        li_gheimat.append(result1)
    for i in range(len(li_name)):
        str1=li_name[i]
        x = str1.find(order_name)

        if x >= 0:
            count+=1
            name=li_name[i]
            desc=li_desc[i]
            gheimat=li_gheimat[i]
            #crusor.execute('insert into car values (\'%s\',\'%s\',\'%s\')' % (name,desc,gheimat))



#cnx.commit()

#cnx.close()