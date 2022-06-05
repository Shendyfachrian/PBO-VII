import cx_Oracle

conn = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE"
)

cur = conn.cursor()
cur.execute("SELECT * FROM golongan")
result = cur.fetchall()

for row in result:
  print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
print("--------------")

cur.execute('''UPDATE golongan
                SET tujangan_suami = %s
                WHERE kode_golongan = %s''', (6000000,'S3'))
conn.commit()

cur.execute("SELECT * FROM golongan")
result = cur.fetchall()

for row in result:
  print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

cur.close()
conn.close()