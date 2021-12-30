from tkinter import *
from login import *

def start(gui):
    gui.geometry("800x900")
    gui.title("ToDo App")
    gui.configure(background='#fef4f4')

    Label(gui,text='Sign Up',bg='#fef4f4',  font=("Arial", 25)).grid(row=2, column=15)

    Label(gui, text="First Name", bg="#fef4f4",width=12).grid(row=3, column=12)
    firstname_field = Entry(gui).grid(row=3, column=15, ipadx="100")

    Label(gui, text="Last Name ", bg="#fef4f4").grid(row=5, column=12)
    lastname_field = Entry(gui).grid(row=5, column=15, ipadx="100")

    Label(gui, text="Email", bg="#fef4f4").grid(row=6, column=12)
    age_field = Entry(gui).grid(row=6, column=15, ipadx="100")

    Label(gui, text="Password", bg="#fef4f4").grid(row=7, column=12)
    password = Entry(gui,show="*",width=20).grid(row=7, column=15,ipadx="100")

    B = Button(gui, text ="Sign UP", command = lambda: But1(gui))

    B.grid(row=8, column=15, ipadx="100")

    B2 = Button(gui, text ="Already Have an Account", command = lambda: But2(gui))

    B2.grid(row=9, column=15, ipadx="100")

def But1(gui):
    gui.destroy()
    calllogin()

def But2(gui):
    gui.destroy()
    calllogin()




def call():
    gui = Tk()
    start(gui)
    gui.mainloop()

call()
