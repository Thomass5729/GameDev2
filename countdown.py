#Clock

from tkinter import *
import time
import tkinter.messagebox

win = Tk()
win.title("My digital countdown")

frame = Frame(win)

hrs_var = StringVar()
min_var = StringVar()
sec_var = StringVar()
hrs_var.set("00")
min_var.set("00")
sec_var.set("00")

hrs_E = Entry(frame,textvariable=hrs_var)
min_E = Entry(frame,textvariable=min_var)
sec_E = Entry(frame,textvariable=sec_var)

def click():
    start_clock.pack_forget()#
    hrs_E.config(state=DISABLED)#
    min_E.config(state=DISABLED)#added this for hwk
    sec_E.config(state=DISABLED)#
    hrs = int(hrs_E.get())
    min = int(min_E.get())
    sec = int(sec_E.get())
    total_seconds = 3600*hrs + 60*min + sec
    while total_seconds > -1:
        minutes = 0
        seconds = 0
        hours = 0
        minutes,seconds = divmod(total_seconds,60)
        if minutes > 60:
            hours,minutes = divmod(minutes,60)
        hrs_var.set("{:02d}".format(hours))
        min_var.set("{:02d}".format(minutes))
        sec_var.set("{:02d}".format(seconds))
        total_seconds-=1
        win.update()
        time.sleep(1)
    
    tkinter.messagebox.showinfo(message="Timer has completed")
    

start_clock = Button(win,text="Start timer",command=click)

hrs_E.grid(row=0,column=0,padx=10)
min_E.grid(row=0,column=1,padx=10)
sec_E.grid(row=0,column=2,padx=10)

frame.pack(pady=50)
start_clock.pack()

win.mainloop()