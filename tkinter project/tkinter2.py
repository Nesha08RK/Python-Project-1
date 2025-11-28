import tkinter as tk
from tkinter import *
from tkinter import ttk   # represent manually

root = tk.Tk()
root.title("Python Tkinter App")
root.geometry("600x400")
label = tk.Label(root, text="Student Application")

#label.pack() #this only shows in center
label.grid(pady=2,padx=20) # this shows in top left corner (dimensions can be given)

root.mainloop()
# the above four lines are common for all the program

