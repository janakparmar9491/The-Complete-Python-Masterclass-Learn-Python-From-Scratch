import psycopg2

conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost",port="5432")
print("Connection success")