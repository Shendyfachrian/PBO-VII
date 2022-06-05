import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pbop12-3"
)

cur = conn.cursor()

cur.execute("INSERT INTO gaji VALUES('Maret','FACHRIAN MAUL',11,0,1,0,5,1000000)")
cur.execute("INSERT INTO gaji VALUES('Juli','ANDIKA PRATAMA',15,4,2,3,5,750000)")
cur.execute("INSERT INTO gaji VALUES('November','ALAN TANI',17,2,4,3,1,500000)")

conn.commit()
cur.close()
conn.close()