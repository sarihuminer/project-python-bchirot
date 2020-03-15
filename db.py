
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                   'Server=comp2;'
                   'Database=bchirot;'
                    'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT  * FROM  party')

for row in cursor:
  print(row)
#import sqlite3

#connection = sqlite3.connect('GovermentElections.db')
#cursor = connection.cursor()

#cursor.execute('CREATE TABLE IF NOT EXIST kalphi()')
#cursor.execute(
 #   'CREATE TABLE IF NOT EXISTS worker(kodworker text primary key,tz text not null,name taxt,phone integer,kodkalphi integer not null primary key references kalphi(numkalphi)')
