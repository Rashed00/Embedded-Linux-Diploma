#!/usr/bin/python3
from tkinter import *

def commnad_handler():
    x = int(entry1.get())
    y = int(entry2.get())
    sum = x + y
    sub = x - y
    if v.get() == 1:
        output = f"The sum is: {x} + {y} = {sum}"
        lbl3 = Label(tab,text=output,background="white",foreground="black")
        lbl3.place(x=180,y=90)
    elif v.get() == 2:
        output = f"The sub is: {x} - {y} = {sub}"
        lbl3 = Label(tab,text=output,background="white",foreground="black")
        lbl3.place(x=180,y=90)
    else:
        print("Please select option.")

tab = Tk()
tab.title("Task[1]")
tab.geometry("420x200+200+200")
tab.resizable(False,False)
tab.configure(background="white")


lbl1 = Label(tab,text="Enter the value of M:",background="white",foreground="black")
lbl2 = Label(tab,text="Enter the value of N:",background="white",foreground="black")
entry1 = Entry(tab,width=10)
entry2 = Entry(tab,width=10)
v = IntVar()
radbut1 = Radiobutton(tab,text='sum',variable=v, value=1)
radbut2 = Radiobutton(tab,text='sub',variable=v, value=2)
but1 = Button(tab,text="Validate",width=(10),command=commnad_handler)

lbl1.place(x=10,y=20)
lbl2.place(x=10,y=50)
entry1.place(x=180,y=20)
entry2.place(x=180,y=50)
radbut1.place(x=10,y=130)
radbut2.place(x=10,y=150)
but1.place(x=180,y=140)


tab.mainloop()




