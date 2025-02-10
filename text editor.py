from tkinter import *
from tkinter.filedialog import asksaveasfile
root = Tk()
root.geometry('400x470')
def save():
     files = [('All files', '*.*'), ('Python files', '*.py'), (' Text Document', '*.txt')]
     file = asksaveasfile(filetypes = files, defaultextension = files)
btn = Button(root, text = 'Save', command = lambda : save())
btn.pack(side = RIGHT)
mainloop()


              
