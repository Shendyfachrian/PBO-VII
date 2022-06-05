import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="pbop12-2"
)

cur = conn.cursor()

cur.execute("SELECT * FROM pegawai")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s,%s,%s,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5]))

cur.close()
conn.close()