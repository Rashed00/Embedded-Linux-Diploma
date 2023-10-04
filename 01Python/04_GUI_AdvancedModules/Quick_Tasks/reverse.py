#!/usr/bin/python3

from tkinter import *

def commnad_handler():
    word = entry1.get()[::-1]
    lbl2 = Label(tab,text=word,background="white",foreground="black")
    lbl2.place(x=120,y=60)

    

    
tab = Tk()
tab.title("Task[1]")
tab.geometry("320x200+200+200")
tab.resizable(False,False)
tab.configure(background="white")

lbl1 = Label(tab,text="Enter a word:",background="white",foreground="black")
but1 = Button(tab,text="Validate",width=(10),command=commnad_handler)
entry1 = Entry(tab,width=15)


lbl1.place(x=10,y=20)
but1.place(x=120,y=100)
entry1.place(x=120,y=20)

tab.mainloop()
