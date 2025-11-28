import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox  # represent manually

root = tk.Tk()
root.title("Python Tkinter App")
root.geometry("600x400")

def Hello():
    label.config(text="Form Submitted Successfully", font=("Arial", 12), fg="green", pady=20, padx=100)
    label.grid(row=1, column=0, columnspan=4, pady=20, sticky="n", ipadx=10, ipady=5)

    messagebox.showinfo("Status....", "App submitted successfully")


label = tk.Label(root, text="Student Application")
label.grid()
#label.grid(pady=2,padx=20) # this shows in top left corner (dimensions can be given)

Button(root, bg="orange", fg="yellow", text="Submit",  font=("Berlin Sans FB", 13), command=Hello).grid(row=3, column=3,padx=100, pady=10)


root.mainloop()


