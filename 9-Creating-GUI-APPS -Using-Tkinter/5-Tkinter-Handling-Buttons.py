from tkinter import *

root = Tk()

def dosomething():
    print("You clicked the button")

button1 = Button(root, text="Click Here", command=dosomething)
button1.pack()

root.mainloop()