from tkinter import *



def startLogin(gui1): 
    gui1.geometry("800x900")    
    gui1.title("login page")  
    gui1.configure(background='#fef4f4') 
    
    Label(gui1, text="login page", font=("Arial", 25),bg="#fef4f4").grid(row=0, column=15)

    Username = Label(gui1, text="Name", font=("Bold", 15),bg="#fef4f4").grid(row=1, column=2)

    password = Label(gui1, text="Password", font=("Bold", 15),bg="#fef4f4").grid(row=2, column=2)

    username_field = Entry(gui1).grid(row=1, column=12, ipadx="50")  
    password_field = Entry(gui1,show="*").grid(row=2, column=12, ipadx="50")  

    Button(text="log in", command=lambda:getvals(gui1)).grid(row=5, column=12)


def getvals(gui1):
    gui1.destroy()
    print("Accepted")






def calllogin():
    print("working")
    gui1 = Tk()
    startLogin(gui1)
    gui1.mainloop
