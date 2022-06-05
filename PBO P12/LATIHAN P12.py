# -*- coding: utf-8 -*-
"""pertemuan12ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/DILANNP/tugas2/blob/main/pertemuan12ipynb.ipynb
"""

# membuat database dan tabel SQlite

import sqlite3

conn = sqlite3.connect("mydb")
cur = conn.cursor()
sql = '''
    CREATE TABLE produk(
      kode CHAR(4) NOT NULL PRIMARY KEY,
      nama VARCHAR(25),
      harga REAL)
      '''
cur.execute(sql)
cur.close()
conn.close

# mengisi tabel produk dalam SQLITE

import sqlite3
conn = sqlite3.connect(mydb)
cur = conn.cursor()

#menambah 3 baris data
cur.execute("INSERT INTO produk VALUES ('P001','Pensil',6000)")
cur.execute("INSERT INTO produk VALUES ('P002','Penghapus',9000)")
cur.execute("INSERT INTO produk VALUES ('P003','Penggaris',12000)")

#commit transaksi
con.commit()

#menutup objek cursor
cur.close()

#menutup Objek koneksi
conn.close()

#membaca baris data dalam sqlite

import sqlite3

conn = sqlite3.connect("mydb")
cur = conn.cursor()
result = cur.execute("SELECT * FROM produk")

#membaca data
for row in result:
  print('%s,%s,%s.of' % (row[0],row[1],row[2]))

cur.close()
conn.close()

# mengubah baris data

import sqlite3

conn = sqlite3.connect("mydb")
cur = conn.cursor()

# data sebelum diubah 
for row in cur.execute("SELECT * FROM produk"):
  print('%s,%s,%s.of' % (row[0],row[1],row[2]))

print("----------------------")

# mengubah data
cur.execute('''UPDATE produk
                 SET harga = ?
                 WHERE kode = ?''', (3000,'P001'))
conn.commit()

#data setelah diubah
for row in cur.execute("SELECT * FROM produk"):
  print('%S,%s,%s.of' % (row[0],row[1],row[2]))

cur.close()
conn.close

# menghapus baris dalam sqlite

import sqlite3

conn = sqlite3.connect("mydb")
cur = conn.cursor()

# data sebelum dihapus
for row in cur.execute("SELECT * FROM produk"):
  print('%s,%s,%s.of' % (row[0],row[1],row[2]))

print("--------------------")

# menghapus data
cur.execute('''DELETE FROM produk
                WHERE kode= ?''', ('P002',))
conn.commit()

# data sebelum dihapus
for row in cur.execute("SELECT * FROM produk"):
  print('%s,%s,%s.of' % (row[0],row[1],row[2]))

cur.close()
conn.close()

# Membuat tabel dari mysql

import mysql.connector

conn = mysql.connector.connect(
    user="roor",
    password="",
    host="localhost",
    database="mydb"
)

cur = conn.cursor()
sql='''
    CREATE TABLE produk (
      kode CHAR(4) NOT NULL PRIMARY KEY,
      nama VARHAR(25),
      harga DECIMAL)
    '''
cur.execute(sql)
cur.close()
conn.close()

#menambah baris data MYsql

import mysql.connector

conn = mysql.connector.connect(
    user="roor",
    password="",
    host="localhost",
    database="mydb"
)

cur = conn.cursor()

#menambah baris data
cur.execute("INSERT INTO produk VALUES ('P001','Pensil',6000)")
cur.execute("INSERT INTO produk VALUES ('P002','Penghapus',9000)")
cur.execute("INSERT INTO produk VALUES ('P003','Penggaris',12000)")

conn.commit()
cur.close()
conn.close()

#menambah baris data

import mysql.connector

conn = mysql.connector.connect(
    user="roor",
    password="",
    host="localhost",
    database="mydb"
)

cur = conn.cursor()

#menambah data
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

#mengubah data
import mysql.connector

conn = mysql.connector.connect(
    user="roor",
    password="",
    host="localhost",
    database="mydb"
)

cur = conn.cursor()
#data sebelum diubah
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))
print("--------------")

#mengubah data
cur.execute('''UPDATE produk SET harga = %s WHERE kode = %s''', (12000,'P002'))
conn.commit()

#data setelah diubah
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# menghapus baris data

import mysql.connector

conn = mysql.connector.connect(
    user="roor",
    password="",
    host="localhost",
    database="mydb"
)

cur = conn.cursor()

# data sebelum dihapus
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))
print("----------")

#menghapus data
cur.execute('''DELETE FROM produk WHERE kode = %s''', ('P002',))
conn.commit()

#data setelah dihapus
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# mwmbuat tabel di postgreSQL

import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pypg")

cur = conn.cursor()
sql = '''
    CREATE TABLE produk (kode CHAR(4) NOT NULL PRIMARY KEY,  nama VARCHAR(25), harga NUMERIC(9,2))'''

cur.execute(sql)
conn.commit()

cur.close()
conn.close()

#menambah baris data didalam postgreSQL

import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pypg")

cur = conn.cursor()
cur.execute("INSERT INTO produk VALUES('P001','Pensil',6000)")
cur.execute("INSERT INTO produk VALUES('P002','Spidol',9000)")
cur.execute("INSERT INTO produk VALUES('P003','Penggaris',12000)")

conn.commit()
cur.close()
conn.close()

# membaca baris data 


import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pypg")

cur = conn.cursor()
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# mengubaH BARIS data



import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pypg")
cur = conn.cursor()

# data sebelum diubah
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))
  print("----------")

# mengubah data
cur.execute('''UPDATE produk SET harga = %s WHERE kode = %s''', (12000,'P002'))
conn.commit()

# data setelah diubah
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# menghapus baris

import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    database="pypg")

cur = conn.cursor()

# data sebelum dihapus
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))
  print("----------")

# menghapus data
cur.execute('''DELETE FROM produk WHERE kode = %s''', ('P002',))
conn.commit()

# data setelah dihapus
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# membuat tabel dalam oracle

import cx_Oracle

conn = cx_Oracle.connect(
    "python"
    "python"
    "127.0.0.1/XE"
)

cur = conn.cursor()
sql = '''
        CREATE TABLE produk (
          kode CHAR (4) NOT NULL PRIMARY KEY,
          nama VARCHAR(25),
          harga DECIMAl
        )
        '''
cur.execute(sql)
cur.close()
conn.close()

#menambah baris data di oracle


import cx_Oracle

con = cx-Oracle.connect(
    "prthon"
    "python"
    "127.0.0.1/XE"
)

cur = conn.cursor()
cur.execute("INSERT INTO produk VALUES('P001','Pensil',6000)")
cur.execute("INSERT INTO produk VALUES('P002','Spidol',9000)")
cur.execute("INSERT INTO produk VALUES('P003','Penggaris',5000)")

conn.commit()
cur.close()
conn.close()

# membaca baris oracle

import cx_Oracle

con = cx-Oracle.connect(
    "prthon"
    "python"
    "127.0.0.1/XE"
)

cur = conn.cursor()
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# mengubah baris oracle

import cx_Oracle

con = cx-Oracle.connect(
    "prthon"
    "python"
    "127.0.0.1/XE"
)

cur = conn.cursor()

#data sebelum diubah
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))
print("-----------------")

# mengubah data 
cur.execute('''UPDATE produk
                SET harga = :1
                WHERE kode = :2''', (12000,'P002'))
conn.commit()

# data setelah diubah
cur.execute("SELECT * fROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()

# menghapus baris data 
import cx_Oracle

con = cx-Oracle.connect(
    "prthon"
    "python"
    "127.0.0.1/XE"
)

cur = conn.cursor()

#data sebelum dihapus
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))
print("-----------------")

# menghapus data
cur.execute('''DELETE FROM produk WHERE kode = :1''', ('P002',))
conn.commit()

#data setelah dihapus
cur.execute("SELECT * FROM produk")
result = cur.fetchall()

for row in result:
  print('%s,%s,%s.of' % (row[[0],row[1],row[2]))

cur.close()
conn.close()