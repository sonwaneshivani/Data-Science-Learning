import mysql.connector 
mydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="shivani@26"
)
mycursor = mydb.cursor() 
# mycursor.execute("select * from test1.test_table") #gives in iterable
''' incase looking for one/ two specific columns '''
mycursor.execute("select c1,c5 from test1.test_table")
for i in mycursor.fetchall(): #Trying to fetch all data
    print(i)