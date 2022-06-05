import sqlite3

conn = sqlite3.connect("pbop12")
cur = conn.cursor()
result = cur.execute("SELECT * FROM jabatan")

for row in result:
  print('%s,%s,%.0f,%.0f' % (row[0],row[1],row[2],row[3]))

cur.close()
conn.close()