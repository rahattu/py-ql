import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='password',
    
)

mycursor=mydb.cursor()

db_name="mydatabase"
sql_command="CREATE DATABASE " + db_name
mycursor.execute(sql_command)