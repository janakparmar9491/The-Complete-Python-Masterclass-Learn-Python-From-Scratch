from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title", "this is awesome")

response = tkinter.messagebox.askquestion("Question 1", "Do like coffee")

if response == 'yes':
    print("Here is a coffee for you")

root.mainloop()