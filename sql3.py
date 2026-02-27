import mysql.connector

connectionstring = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "siws",
    database = "vscb1"
    )
print(connectionstring)
cursor1 = connectionstring.cursor()

print(cursor1)
sqlquery1 = "create table student(srno int, sname varchar(30))"
cursor1.execute(sqlquery1)
print("Table created")
connectionstring.close()
