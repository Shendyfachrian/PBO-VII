import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pbop12-3"
)

cur = conn.cursor()

cur.execute("SELECT * FROM gaji")
result = cur.fetchall()

for row in result:
  print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
print("--------------")

cur.execute('''UPDATE gaji SET potongan = %s WHERE nip = %s''', (1500000,'TABIA HANURAL'))
conn.commit()

cur.execute("SELECT * FROM gaji")
result = cur.fetchall()

for row in result:
  print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

cur.close()
conn.close()