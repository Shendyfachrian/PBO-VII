import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="pbop12-2"
)

cur = conn.cursor()
sql='''
    CREATE TABLE pegawai (
      nip  VARCHAR(20) NOT NULL PRIMARY KEY,
      nama_pegawai  VARCHAR(40),
      kode_jabatan VARCHAR(3),
      kode_golongan  VARCHAR(3),
      status  VARCHAR(15),
      jumlah_anak  INT(2))
      '''
cur.execute(sql)
cur.close()
conn.close()