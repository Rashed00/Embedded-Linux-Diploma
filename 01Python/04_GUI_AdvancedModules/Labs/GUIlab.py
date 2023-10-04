#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

def command_handler():
    print("You're logged in.")
    

def items_selected(event):
    #get selected indices
    selected_index = listbox1.curselection()
    #get selected items
    print(listbox1.get(selected_index))

window = Tk()
window.title("Python GUI")
window.geometry("500x500+200+200")
window.resizable(False,False)
window.configure(background="blue")
frame1 = Frame(window, width=250,height=500)
# frame2 = Frame(window, width=250,height=500)


#handlers
lbl1 = Label(window,text="First name",background="white",foreground="black")
lbl2 = Label(window,text="Second name",background="white",foreground="black")
lbl3 = Label(frame1,text="Rate this GUI",background="white",foreground="black")
entry1 = Entry(window,width=10)
entry2 = Entry(window,width=10)
but1 = Button(window,text="Login",width=(10),command=command_handler)
but2 = Button(window,text="Stop",width=(25),command=window.destroy)
listbox1 = Listbox(frame1)
listbox1.insert(1,'Python')
listbox1.insert(2,'C++')
listbox1.insert(3,'Java')
listbox1.insert(4,'Others')
v = IntVar()
radbut1 = Radiobutton(window,text='sum',variable=v, value=1)
radbut2 = Radiobutton(window,text='sub',variable=v, value=2)
check = Checkbutton(window,text="Null")
scale = Scale(frame1,from_=0,to=10, orient=HORIZONTAL)

#formatting
# lbl1.grid(row=0,column=0)
# lbl2.grid(row=1,column=1)
# lbl3.grid(row=2,column=2)
lbl1.place(x=10,y=50)
lbl2.place(x=10,y=70)
lbl3.place(x=0,y=220)
entry1.place(x= 120, y = 50)
entry2.place(x= 120, y=70)
but1.place(x=10,y=90)
but2.place(x = 250, y=280)
listbox1.place(x = 0,y=0)
radbut1.place(x=10,y=120)
radbut2.place(x=10,y=140)
check.place(x=10,y=160)
scale.place(x=0,y=240)
frame1.place(x=250,y=0)
# frame2.place(x=250,y=0)



listbox1.bind('<<ListboxSelect>>', items_selected)
window.mainloop()


