import psycopg2
import sqlite3


try:
	conn = psycopg2.connect(dbname='dfu5v18hea0jro', user='puxsikmrnjnnml', host='ec2-107-22-175-206.compute-1.amazonaws.com', password='fpqWwIT73lFClOn23I1MMYpjP3', port='5432') 
except:
	print "I am unable to connect to the database"

cur = conn.cursor()
try:
    cur.execute("""SELECT * FROM pheno_db""")
except:
    print "I can't SELECT from pheno_db"

rows = cur.fetchall()



conn_sql = sqlite3.connect('genoweb/db.sqlite3')
cursor = conn_sql.cursor()

for row in rows:
    print "   ", row
    conn_sql.execute("INSERT OR REPLACE INTO genes_phenodb values (?, ?, ?)", row)
conn_sql.commit()
conn.close()
conn_sql.close()