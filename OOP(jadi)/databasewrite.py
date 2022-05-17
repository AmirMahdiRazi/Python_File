import mysql.connector

cnx = mysql.connector.connect(user="root",password="Razi0023161469",host="127.0.0.1",database="learn")


crusor=cnx.cursor()


crusor.execute('insert into people values (\'far\',\'f\',35)')

cnx.commit()


cnx.close()