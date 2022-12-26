import tkinter as tk
from tkinter import *
from tkinter import ttk

class pos():
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.window1()
    def window1(self):
        # Delete old frame?
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(self.master, width=300, height=300)
        # Page layout
        pg2_button = tk.Button(text = "pg 2", command = self.window2).grid(column=1, row=5)
        name = tk.Entry().grid(column=2, row=1)
        phone = tk.Entry().grid(column=2, row=2)
        get_name = tk.Label(text = "Name: ").grid(column = 1, row = 1)
        get_phone = tk.Label(text = "Phone: ").grid(column = 1, row = 2)
       


    def window2(self):
        # Delete old frame?
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = tk.Frame(self.master, width=300, height=300)
        # Page layout
        pg2_button = tk.Button(text = "pg 1", command = self.window1).grid(column=1, row=5)
        b = tk.Label(text = "or").grid(column = 1, row = 1)
        
root = Tk()
root.title("POS")
pos(root)
root.mainloop()

