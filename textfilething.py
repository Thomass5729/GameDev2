from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile


win = Tk()
win.title("Textfilething")

def openfile():
    var = askopenfile(mode="r",filetypes=[("python files","*.py")])
    if var != None:
        read = var.read()
        print(read)

def savefile():
    files=[("all files","*.*"), ("python files","*.py"), ("text document","*.txt")]
    var2 = asksaveasfile(filetypes=files,defaultextension=files)

frame = Frame(win)
save = Button(win,text="Save",command=savefile)
entry = Entry(win)
add = Button(win,text="Add")
open = Button(frame,text="Open",command=openfile)
scrollbar = Scrollbar(frame,orient="vertical")
box = Listbox(frame,width=70,yscrollcommand=scrollbar.set,bg="grey")
scrollbar.config(command=box.yview)
delete = Button(frame,text="Delete")

for i in range(50):
    box.insert(END,f"List {i}")


save.pack(pady=3)
entry.pack(pady=3)
add.pack(pady=3)
frame.pack(pady=3)
open.grid(row=0,column=0,padx=4)
box.grid(row=0,column=1,padx=4)
scrollbar.grid(row=0,column=2)
delete.grid(row=0,column=3,padx=4)
mainloop()