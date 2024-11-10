#ROCK PAPER SCISSORS

from tkinter import *
import random


win = Tk()
win.config(bg="white")
win.geometry("+400+250")
options = ["rock","paper","scissors"]


greenlist = ["Lets start the game","YOU WIN!","YOU LOSE!","TIE!"]
pscore = 0
cscore = 0


def mainloop(option):
    computer_choice = random.choice(options)
    playerselectlabel.config(text=f"You selected: "+option)
    computerselectlabel.config(text=f"Computer selected: "+computer_choice)
    if option == computer_choice:
        tie()
    elif option == options[0] and computer_choice == options[1]:
        player_loss()
    elif option == options[0] and computer_choice == options[2]:
        player_win()
    elif option == options[1] and computer_choice == options[2]:
        player_loss()
    elif option == options[1] and computer_choice == options[0]:
        player_win()
    elif option == options[2] and computer_choice == options[0]:
        player_loss()
    elif option == options[2] and computer_choice == options[1]:
        player_win()

def tie():
    global greenlabel,playerscorelabel,computerscorelabel
    greenlabel.config(text=greenlist[3])
    playerscorelabel.config(text=f"Player score: {pscore}")
    computerscorelabel.config(text=f"Player score: {cscore}")
def player_win():
    global greenlabel,playerscorelabel,computerscorelabel,pscore
    greenlabel.config(text=greenlist[1])
    pscore+=1
    playerscorelabel.config(text=f"Player score: {pscore}")
    computerscorelabel.config(text=f"Player score: {cscore}")
def player_loss():
    global greenlabel,playerscorelabel,computerscorelabel,cscore
    greenlabel.config(text=greenlist[2])
    cscore+=1
    playerscorelabel.config(text=f"Player score: {pscore}")
    computerscorelabel.config(text=f"Computer score: {cscore}")




'''def player_win():
    exit()'''



 
title = Label(win,text="ROCK PAPER SCISSORS",font=("arial",60,"normal"))
greenlabel = Label(win,text=greenlist[0],font=("arial",25,"normal"),fg="green")
frame = Frame(win)

optlabel = Label(frame,text="Your Options:",font=("arial",25,"normal"))
rock_but = Button(frame,text="Rock",bg="pink",font=("arial",25,"normal"),command=lambda: mainloop(options[0]))
paper_but = Button(frame,text="Paper",bg="Grey",font=("arial",25,"normal"),command=lambda: mainloop(options[1]))
scissors_but = Button(frame,text="Scissors",bg="Blue",font=("arial",25,"normal"),command=lambda: mainloop(options[2]))
scorelabel = Label(frame,text="Score:",font=("arial",25,"normal"))
playerselectlabel = Label(frame,text=f"You selected: ",font=("arial",25,"normal"))
computerselectlabel = Label(frame,text=f"Computer selected: ",font=("arial",25,"normal"))
playerscorelabel = Label(frame,text=f"Player score: {pscore}",font=("arial",25,"normal"))
computerscorelabel = Label(frame,text=f"Computer score: {cscore}",font=("arial",25,"normal"))



title.pack()
greenlabel.pack()
frame.pack()
optlabel.grid(row=0,column=0,pady=5)
rock_but.grid(row=2,column=2,pady=5)
paper_but.grid(row=2,column=3,pady=5)
scissors_but.grid(row=2,column=4,pady=5)
scorelabel.grid(row=3,column=0,pady=5)
playerselectlabel.grid(row=4,column=2,pady=5)
computerselectlabel.grid(row=4,column=3,pady=5)
playerscorelabel.grid(row=5,column=2,pady=5)
computerscorelabel.grid(row=5,column=3,pady=5)

win.mainloop()