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

sqlquery1 = "SELECT curdate()"
cursor1.execute(sqlquery1)
row1 = cursor1.fetchone()
print(row1[0])

connectionstring.close()
