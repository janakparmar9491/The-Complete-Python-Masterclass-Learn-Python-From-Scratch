from tkinter import *

root = Tk()

lable1 = Label(root, text="First", bg="Red",fg="White")
lable1.pack(fill=X)

lable2 = Label(root, text="Second", bg="Blue",fg="White")
lable2.pack(side=LEFT, fill=Y)

root.mainloop()