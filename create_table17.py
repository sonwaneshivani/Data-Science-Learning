#Refer day17.py for documentation
#Creating table and database

import mysql.connector 
mydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="shivani@26"
)
mycursor = mydb.cursor() 
mycursor.execute("CREATE DATABASE if not exists test1") #Query for creating new DB's test1
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT, c2 VARCHAR(50),c3 INT, c4 FLOAT, c5 VARCHAR(40))") #Query for creating table here we have to specify databasename.tablename
mydb.close()