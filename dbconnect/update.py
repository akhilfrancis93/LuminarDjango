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

sql="update student set total=600 where stid=100"

cursor.execute(sql)

db.commit()

#data=cursor.fetchone()
#print(data)