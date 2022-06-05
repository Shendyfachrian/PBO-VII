import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pbop12-3"
)

cur = conn.cursor()
sql='''
    CREATE TABLE gaji (
      bulan  VARCHAR(20) NOT NULL PRIMARY KEY,
      nip  VARCHAR(20),
      masuk INT(5),
      sakit  INT(5),
      ijin  INT(5),
      alpha  INT(5)
      lembur  INT(5)
      potongan  INT(10))
      '''
cur.execute(sql)
conn.commit()

cur.close()
conn.close()