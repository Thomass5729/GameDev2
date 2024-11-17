#Guess my number

from tkinter import *
import random
import tkinter.messagebox

win = Tk()
win.config(bg="white")
win.minsize(350,250)
win.title("Guess my number")
rand_num = random.randint(0,20)
tries = 0

def ok_b():
    name = nameE.get()
    tkinter.messagebox.showinfo(title="Popup",message="Hello "+name+" I am thinking of a number from 1 to 20. Try and guess it!",detail="Bet you can't!")

def guess_click():
    global tries
    num_guess = int(guessE.get())
    tries += 1
    if num_guess == rand_num:
        tkinter.messagebox.showinfo(message="You guessed the right number!",detail=f"It took you {tries} tries")
    elif num_guess < rand_num:
        tkinter.messagebox.showinfo(message="You guessed incorrectly!. You are too low.")
    elif num_guess > rand_num:
        tkinter.messagebox.showinfo(message="You guessed incorrectly!. You are too high.")

    

welcomeL = Label(win,text="Welcome to our game",font=40)

welcomeL.pack(pady=30)
frame = Frame(win)

asknameL= Label(frame,text="What is your name?",font=40)
nameE = Entry(frame,font=40)
okB = Button(frame,text="OK",font=40,command=ok_b)
takeguessL= Label(frame,text="Take a guess:",font=40)
guessE = Entry(frame,font=40)
guessB = Button(frame,text="Guess",font=40,command=guess_click)

frame.pack()
asknameL.grid(row=0,column=0)

nameE.grid(row=1,column=0)
okB.grid(row=1,column=1,pady=10)
takeguessL.grid(row=2,column=0)
guessE.grid(row=3,column=0)
guessB.grid(row=3,column=1)


win.mainloop()