import mysql.connector


afrad = ["Amin",75,180,"Mahdi",90,190,"Mohammad",75,175,"Ahmad",60,175]

cnx = mysql.connector.connect(user="root",password="Razi0023161469",host="127.0.0.1",database="work")


crusor=cnx.cursor()

num=int(input("Number of Employees :"))
afrad=[]
for num in range(num):
    str1=input("Name, weight and height of the employee :")

    afrad=str1.split(" ")
        
    name=afrad[0]
    weight=int(afrad[1])
    height=int(afrad[2])
    crusor.execute('insert into people values (\'%s\',%i,%i)' % (name,weight,height))

cnx.commit()

cnx.close()








