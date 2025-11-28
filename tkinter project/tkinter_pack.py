import tkinter as tk
from tkinter import *
from tkinter import ttk   # represent manually

root = tk.Tk()
root.title("Python Tkinter App")
root.geometry("600x400")



label = tk.Label(root, text="Student Application", font=("Arial", 20))

label.pack() #this only shows in center
but = tk.Button(root, background="grey", foreground="white", text="Submit", font=("Berlin Sans FB", 13))
but.pack()
Button(root, bg="blue", fg="yellow", text="Submit").pack()
root.mainloop()


