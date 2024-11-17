#Clock

from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

win = Tk()
win.title("My digital clock")

def time():
    currenttime = strftime("%d/%m/%Y %H:%M:%S %p")
    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray', 'dimgray', 'LightSlateGray','AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']
    clocklabel.config(text=currenttime,background=random.choice(color_list),foreground=random.choice(color_list))
    clocklabel.after(1000,time)



clocklabel = Label(win,font=("arial",50,"bold"),background="grey",foreground="red")

clocklabel.pack()

time()
win.mainloop()