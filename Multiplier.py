
from tkinter import *
from tkinter.ttk import *


win = Tk()
win.title("Multipication tables")

def muliplier():
    multiples = ""
    for i in range(0,num2.get()+1):
        multiples+=f"\n{num.get()} x {i} = {i*num.get()}"
    muliples.configure(text=multiples)



frame = Frame(win)

title = Label(win,text="Multiplier")
info = Label(frame,text="Pick a number and a range:")
num = IntVar()
dropdown = Combobox(frame,textvariable=num,width=5)
dropdown["values"]=tuple(range(51))
num2 = IntVar()
r1 = Radiobutton(frame,text="10",variable=num2,value=10)
r2 = Radiobutton(frame,text="20",variable=num2,value=20)
r3 = Radiobutton(frame,text="30",variable=num2,value=30)
button = Button(win,text="Go",command=muliplier)
muliples = Label(win,anchor="center",text="")


title.pack()
frame.pack()
info.grid(row=1,column=0,padx=4)
dropdown.grid(row=1,column=1,padx=4)
r1.grid(row=0,column=2,padx=4)
r2.grid(row=1,column=2,padx=4)
r3.grid(row=2,column=2,padx=4)
button.pack()
muliples.pack()


mainloop()