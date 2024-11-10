#Clock

from tkinter import *
from tkinter.ttk import *
from time import strftime

win = Tk()
win.title("Clock")

def time():
    currenttime = strftime("%d/%m/%Y %H:%M:%S %p")

    clocklabel.config(text=currenttime)
    clocklabel.after(1000,time)


clocklabel = Label(win,font=("arial",50,"bold"),background="grey",foreground="red")

clocklabel.pack()

time()
win.mainloop()