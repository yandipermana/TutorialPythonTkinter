from tkinter import *
from tkinter import Menubutton

top = Tk()

mb = Menubutton = Menubutton(top, text="condiments", relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

mb.pack()
top.mainloop()

