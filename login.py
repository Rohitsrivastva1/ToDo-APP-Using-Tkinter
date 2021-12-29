from tkinter import *
from tkinter import font
from typing import Sized

gui = Tk()   
gui.geometry("800x900")    
gui.title("login page")  
gui.configure(background='#fef4f4') 

def getvals():
    print("Accepted")

Label(gui, text="login page", font=("Arial", 25)).grid(row=0, column=15)

Username = Label(gui, text="Name", font=("Bold", 15)).grid(row=1, column=2)

password = Label(gui, text="Password", font=("Bold", 15)).grid(row=2, column=2)

username_field = Entry(gui).grid(row=1, column=12, ipadx="50")  
password_field = Entry(gui,show="*").grid(row=2, column=12, ipadx="50")  

Button(text="log in", command=getvals).grid(row=5, column=12)
gui.mainloop()
