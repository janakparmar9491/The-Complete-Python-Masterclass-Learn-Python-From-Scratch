import psycopg2

conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost",port="5432")
cur = conn.cursor()
cur.execute('''create table students(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')
print("Table created")
conn.commit()
conn.close()
