import mysql.connector

connectionstring = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "siws"
    )
print(connectionstring)

cursor1 = connectionstring.cursor()
print(cursor1)

sqlquery1 = "create database vscb1"
cursor1.execute(sqlquery1)

connectionstring.close()
