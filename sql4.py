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
sqlquery1 = "INSERT INTO student(srno,sname) VALUES(%s,%s)"
sqlvalues = (19037,"Sabari")
cursor1.execute(sqlquery1,sqlvalues)
connectionstring.commit()
print("record inserted")
print(cursor1.rowcount)

connectionstring.close()
