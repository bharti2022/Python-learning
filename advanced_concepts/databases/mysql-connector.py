import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',user= 'root',passwd= '')
cursor = conn.cursor()

cursor.execute("SELECT * FROM ecomdb")

# get a single row
row = cursor.fetchone()
print(row)

# disconnect from the database
conn.close()