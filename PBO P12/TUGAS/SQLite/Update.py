import sqlite3

conn = sqlite3.connect("pbop12")
cur = conn.cursor()

for row in cur.execute("SELECT *FROM jabatan"):
  print('%s,%s,%.0f,%.0f' % (row[0],row[1],row[2],row[3]))

print("--------------")

cur.execute('''UPDATE jabatan
               SET tunjangan_jabatan = ?
               WHERE kode_jabatan = ? ''', (750000,'JKW'))
conn.commit()

for row in cur.execute("SELECT *FROM jabatan"):
  print('%s,%s,%.0f,%.0f' % (row[0],row[1],row[2],row[3]))

cur.close()
conn.close()