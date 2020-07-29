import psycopg2

def create():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute('''create table students(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')
    print("Table created")
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute('''INSERT INTO students (NAME, AGE, ADDRESS) VALUES('John', '25', 'NY');''')
    print("One Record Inserted.")
    conn.commit()
    conn.close()

insert_data()