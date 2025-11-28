import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox  # represent manually

root = tk.Tk()
root.title("Python Tkinter App")
root.geometry("800x400")

def Hello():
    label.config(text="Form Submitted Successfully", font=("Arial", 12), fg="green", pady=20, padx=100)
    label.grid(row=1, column=3, columnspan=4, pady=20, sticky="n", ipadx=10, ipady=5)

    messagebox.showinfo("Status....", "App submitted successfully")


label = tk.Label(root, text="Student Application", font=("Arial", 20))
label.grid( row=1, column=3,padx=100, pady=10)
#label.grid(pady=2,padx=20) # this shows in top left corner (dimensions can be given)


rb1 = Radiobutton(root, text="Male", value=1, font=("Arial", 14))
rb1.grid(row=2, column=3, padx=10, pady=10)
rb2 = Radiobutton(root, text="Female", value=2, font=("Arial", 14))
rb2.grid(row=3, column=3, padx=10, pady=10)
Button(root, bg="orange", fg="yellow", text="Submit",  font=("Berlin Sans FB", 13), command=Hello).grid(row=4, column=3,padx=100, pady=10)

ent1 = Entry(root, width=50, font=("Arial", 14), borderwidth=10, bg="light grey", fg="dark blue")
ent1.grid(row=5, column=3, padx=450, pady=10)

ent2 = Entry(root, width=50, font=("Arial", 14), borderwidth=10, bg="sky blue", fg="dark blue")
ent2.grid(row=6, column=3, padx=450, pady=10)

cb1 = ttk.Combobox(root, textvariable=5, width=20, height=14)
cb1['values'] = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]
cb1.grid(row=7, column=3, padx=100, pady=10)

btn2 =  Button(root, bg="orange", fg="yellow", text="Submit",  font=("Berlin Sans FB", 13), command=Hello)
btn2.grid(row=8, column=3)

root.mainloop()


