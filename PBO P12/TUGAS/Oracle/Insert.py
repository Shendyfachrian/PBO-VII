import cx_Oracle

conn = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE"
)

cur = conn.cursor()
cur.execute("INSERT INTO golongan VALUES('D3','DIPLOMA 3',1000000,250000,10000,100000,1000000)")
cur.execute("INSERT INTO golongan VALUES('S1','SARJANA 1',3000000,500000,20000,100000,1000000)")
cur.execute("INSERT INTO golongan VALUES('S3','SARJANA 3',5000000,1000000,30000,100000,1000000)")

conn.commit()
cur.close()
conn.close()