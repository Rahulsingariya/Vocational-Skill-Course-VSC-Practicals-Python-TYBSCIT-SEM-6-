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
sqlquery1 = "SELECT * from student"


cursor1.execute(sqlquery1)
print(cursor1)
resultset1=cursor1.fetchall()
print(resultset1)

for res in resultset1:
    print(res)

connectionstring.close()
