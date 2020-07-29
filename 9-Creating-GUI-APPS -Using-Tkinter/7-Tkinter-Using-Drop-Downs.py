from tkinter import *

def function1():
    print("Menu Item Clicked.")

root = Tk()

mymenu = Menu(root)

submenu = Menu(mymenu)
#mymenu.add_cascade(lable="File", menu=submenu)

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)
submenu.add_separator()
submenu.add_command(label="Exit", command=function1)


mymenu.add_cascade(label="File", menu=submenu)

newmenu = Menu(mymenu)

newmenu.add_command(label="Redo", command=function1)
newmenu.add_command(label="Undo", command=function1)
mymenu.add_cascade(label="Edit", menu=newmenu)


root.config(menu=mymenu)
root.mainloop()