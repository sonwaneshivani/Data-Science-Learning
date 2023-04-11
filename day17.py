import mysql.connector #calling
'''communication part'''
#To connect
mydb = mysql.connector.connect(
    host="localhost", #Host name could this the ip address(127.0.0.1@3306),it means local system
    user="root",
    password="shivani@26"
)
#The above establishes the communication btwn python file & sql database 
print(mydb) #printing the connections


#To store data/create table,etc has to be done wrto my connectivity we established
mycursor = mydb.cursor() #This enables us to execute any queries. bcoz in DB's we need cursor to peform these kind of operations
mycursor.execute("SHOW DATABASES") #executing one command, we can try to call inside cursor.execute fun and can pass our own sql command & gives iterable outcome
for x in mycursor:
    print(x)
#It is showing all the existing DB's inside mysql(test was created by us & rest all are inbuilt/default)

'''We can try to execute same command inside sql also.  Then why are we building in python bcoz we have to build entire application in python'''

#Query Creating Table in newfile(create_table) for clean code