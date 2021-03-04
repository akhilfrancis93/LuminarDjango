#step1 import mysql connector
import mysql.connector

#step2 establish connection
db=mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="Dejavu123@",
    auth_plugin="mysql_native_password",
    database="student"
)

#step3 create a cursor object

cursor=db.cursor()

sql="create table stude nt(stid int,name varchar(30),total varchar(20))"

cursor.execute(sql)

#data=cursor.fetchone()
#print(data)