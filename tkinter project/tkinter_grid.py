import tkinter as tk
from tkinter import *
from tkinter import ttk   # represent manually

root = tk.Tk()
root.title("Python Tkinter App")
root.geometry("600x400")
label = tk.Label(root, text="Student Application")

label.grid()
#label.grid(pady=2,padx=20) # this shows in top left corner (dimensions can be given)
but = tk.Button(root, background="grey", foreground="white", text="Submit")
but.grid()
Button(root, bg="red", fg="yellow", text="Submit").grid()
root.mainloop()


