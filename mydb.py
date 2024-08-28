import mysql.connector


dataBase= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= '1234'
)

# prepare a cursor object
curserObject = dataBase.cursor()

# create a database
curserObject.execute("CREATE DATABASE company")
print("database created!")


