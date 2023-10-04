#!/usr/bin/python3

from tkinter import *

def commnad_handler(event):
    pass

tab = Tk()
tab.title("Task[1]")
tab.geometry("320x200+200+200")
tab.resizable(False,False)
tab.configure(background="white")

but1 = Button(tab,text="Button1",width=(10),command=commnad_handler)
but2 = Button(tab,text="Button2",width=(10),command=commnad_handler)
but3 = Button(tab,text="Button3",width=(10),command=commnad_handler)
but4 = Button(tab,text="Button4",width=(10),command=commnad_handler)

but1.grid(row=0,column=1)
but2.grid(row=1,column=0)
but3.grid(row=1,column=2)
but4.grid(row=2,column=1)

tab.mainloop()
