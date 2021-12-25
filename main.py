from tkinter import *
from typing import Sized


gui = Tk()
gui.geometry("800x900")
gui.title("ToDo App")
gui.configure(background='#fef4f4')

Label(gui,text='Sign Up',bg='#fef4f4',   font=("Arial", 25)).grid(row=2, column=15)

Label(gui, text="First Name", bg="#fef4f4",width=12).grid(row=3, column=12)
firstname_field = Entry(gui).grid(row=3, column=15, ipadx="100")
Label(gui, text="Last Name ", bg="#fef4f4").grid(row=5, column=12)
lastname_field = Entry(gui).grid(row=5, column=15, ipadx="100")
Label(gui, text="Age", bg="#fef4f4").grid(row=6, column=12)
age_field = Entry(gui).grid(row=6, column=15, ipadx="100")







mainloop()
