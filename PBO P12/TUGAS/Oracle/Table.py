import cx_Oracle

conn = cx_Oracle.connect(
    "python",   #username
    "python",   #password
    "127.0.0.1/XE"
)

cur = conn.cursor()
sql='''
    CREATE TABLE golongan (
      kode_golongan  VARCHAR(3) NOT NULL PRIMARY KEY,
      nama_golongan  VARCHAR(10),
      tunjangan_suami INT(10),
      tunjangan_anak  INT(10),
      uang_makan  INT(10),
      uang_lembur  INT(10),
      askes  INT(10)
    )
      '''
cur.execute(sql)
cur.close()
conn.close()