# Database connection
import mysql.connector as mysql
# create the MySQL database connection
mydb = mysql.connect(host='localhost', user='Peter',password='1234', database='World')

# setup the cursor
mycursor = mydb.cursor()
# execute the SQL command
mycursor.execute('show databases')
# store the result to somewhere
result = mycursor.fetchall()
for i in result:
    print(i)

print('*'*20)

mycursor.execute('select * from city')
# print the content of executed SQL command
for i in mycursor:
    print(i)