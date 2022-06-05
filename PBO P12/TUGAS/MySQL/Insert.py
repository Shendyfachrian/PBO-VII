import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="pbop12-2"
)

cur = conn.cursor()

cur.execute("INSERT INTO pegawai VALUES('AAA','Birma','BRM','BBB','Aktif',2)")
cur.execute("INSERT INTO pegawai VALUES('BBB','Annisa','DZU','DDD','Aktif',5)")
cur.execute("INSERT INTO pegawai VALUES('CCC','Sabila','EFA','EEE','Aktif',4)")

conn.commit()
cur.close()
conn.close()