import mysql.connector


    
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='password',
    database="mydatabase"
    

)

mycursor=mydb.cursor()

sql_command = """
                     UPDATE  student 
                     SET first_name="tamim"
                     where roll=1
                     

"""
mycursor.execute(sql_command)
mydb.commit()