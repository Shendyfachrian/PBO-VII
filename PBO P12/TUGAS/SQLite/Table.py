import sqlite3

conn = sqlite3.connect("pbop12")
cur = conn.cursor()
sql = '''
    CREATE TABLE jabatan (
    kode_jabatan VARCHAR(3) NOT NULL PRIMARY KEY,
    nama_jabatan VARCHAR(40),
    gapok INT(10),
    tunjangan_jabatan INT(10))
     '''
cur.execute(sql)
cur.close()
conn.close()