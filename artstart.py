from tkinter import *
import tkinter.ttk
root = Tk()
root.title=("Art Start")
root.geometry("300x100")

def nextPage():
    root.destroy()
    import artmain

btn = Button(text = 'Enter the Turtle Art Place', border = '10', command=nextPage).pack(side = 'top')


mainloop()