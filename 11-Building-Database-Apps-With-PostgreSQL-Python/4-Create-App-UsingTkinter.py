from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(name, age, address):
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO students (NAME, AGE, ADDRESS) VALUES(%s, %s, %s);'''
    cur.execute(query, (name, age, address))
    print("One Record Inserted.")
    conn.commit()
    conn.close()

def search(id):
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM students WHERE ID=%s;'''
    cur.execute(query, (id))
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox = Listbox(frame, width=20,height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)

def display_all():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="root", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM students;'''
    cur.execute(query)
    row = cur.fetchall()
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10, column=1)
    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()



canvas = Canvas(root, height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8, relheight=0.8)

lable = Label(frame, text="Add Data")
lable.grid(row=0, column=1)

name = Label(frame, text="Name")
name.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

age = Label(frame, text="Age")
age.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

address = Label(frame, text="Address")
address.grid(row=3, column=0)
entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text="Add", command=lambda: get_data(entry_name.get(),entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

lable = Label(frame, text="Search")
lable.grid(row=5, column=1)

lable = Label(frame, text="Search By ID")
lable.grid(row=6, column=0)
id_search = Entry(frame)
id_search.grid(row=6, column=1)
button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=6, column=2)

display_all()
root.mainloop()