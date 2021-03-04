import mysql.connector

db=mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="Dejavu123@",
    auth_plugin="mysql_native_password",
    database="student"
)

cursor=db.cursor()

sql="insert into student values('100','akhil','550')"

cursor.execute(sql)

db.commit()

#data=cursor.fetchone()
#print(data)