import sqlite3

conn = sqlite3.connect("pbop12")
cur = conn.cursor()

cur.execute("INSERT INTO jabatan VALUES('JKW','Ketua',3000000,500000)")
cur.execute("INSERT INTO jabatan VALUES('MAM','Wakil Ketua',2000000,250000)")
cur.execute("INSERT INTO jabatan VALUES('THR','Bendahara',1000000,100000)")

conn.commit()

cur.close()

conn.close()