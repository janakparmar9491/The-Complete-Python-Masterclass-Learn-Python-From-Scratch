from tkinter import *


root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0, 200, 100, fill="green")

root.mainloop()