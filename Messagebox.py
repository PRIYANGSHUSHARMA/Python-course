from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x600")

def msg():
     messagebox.showwarning("Alert", "Please stop virus detected")

def msg2():
     messagebox.askokcancel("Help", "Please confirm")     

button = Button(root, text="Scan for the Virus", command = msg) 
button = Button(root, text="Ok or cancel", command = msg2) 
button.place(x = 40, y = 80)
button.place(x = 141, y = 180 )
root.mainloop()
