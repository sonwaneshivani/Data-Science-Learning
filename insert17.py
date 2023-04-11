import mysql.connector 
mydb = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="shivani@26"
)
mycursor = mydb.cursor() 
mycursor.execute("insert into test1.test_table values(1234, 'shivi',234,34.0,'pinky')") #use single quotes for string or else it gives error
'''can insert same/dffrnt data multiple tyms'''
mycursor.execute("insert into test1.test_table values(1234, 'shivi',234,34.0,'pinky')") #use single quotes for string or else it gives error
mycursor.execute("insert into test1.test_table values(1234, 'shivi',234,34.0,'pinky')") #use single quotes for string or else it gives error
mycursor.execute("insert into test1.test_table values(1234, 'shivi',234,34.0,'pinky')") #use single quotes for string or else it gives error
mycursor.execute("insert into test1.test_table values(1234, 'shivi',234,34.0,'pinky')") #use single quotes for string or else it gives error

mydb.commit() #always try to call it, so it makes changes permanent
mydb.close()

# Checking for the data that we stored in query.py file. for clean code