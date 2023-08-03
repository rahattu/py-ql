import mysql.connector


    
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='password',
    database="hr"
    

)

mycursor=mydb.cursor()

sql_command = """
select *
from employees
where salary > 2000
limit 5




"""
mycursor.execute(sql_command)
data=mycursor.fetchall()
for i in data:
     print(i)
