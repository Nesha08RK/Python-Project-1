import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

def Ok():
    username = e1.get()
    password = e2.get()
    if username == "admin" and password == "12345":
        messagebox.showinfo("Login Status", "Login Successful")
        root.destroy()
    elif username == "" and password == "":
        messagebox.showwarning("Login Status", "Please enter Username and Password")
    else:
        messagebox.showerror("Login Status", "Invalid Username or Password")

global e1
global e2

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
Button(root, text="Login", command= Ok, height=2, width=13).place(x=100, y=100)


root.mainloop()