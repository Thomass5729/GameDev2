#Guess my number

from tkinter import *
import random
import tkinter.messagebox

win = Tk()
win.config(bg="white")
win.minsize(350,250)
win.title("Guess my number")


welcomeL = Label(win,text="Welcome to our game",font=40)

welcomeL.pack(pady=30)
frame = Frame(win)

asknameL= Label(frame,text="What is your name?",font=40)
nameE = Entry(frame,font=40)
okB = Button(frame,text="OK",font=40)
takeguessL= Label(frame,text="Take a guess:",font=40)
guessE = Entry(frame,font=40)
guessB = Button(frame,text="Guess",font=40)

frame.pack()
asknameL.grid(row=0,column=0)

nameE.grid(row=1,column=0)
okB.grid(row=1,column=1,pady=10)
takeguessL.grid(row=2,column=0)
guessE.grid(row=3,column=0)
guessB.grid(row=3,column=1)


win.mainloop()