import mysql.connector

cnx = mysql.connector.connect(user="root",password="Razi0023161469",host="127.0.0.1",database="learn")


crusor=cnx.cursor()

query = "SELECT * FROM people;"
crusor.execute(query)

for (name , sex , age) in crusor:
    print(name ,sex,age)

cnx.close()