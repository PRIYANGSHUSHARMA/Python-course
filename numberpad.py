from tkinter import *
root = Tk()
root.title('Number Pad')
root.geometry('250x300')
nums = [[109,108,107], [106,105,104], [103,102,101], ['#','0','*']]
for i in range (4):
     for j in range(0,3):
          frame = Frame(master = root, relief = RIDGE, borderwidth=1)
          frame.grid(row = i, column = j)
          label = Label(master = frame, text= nums[i][j], bg = '#2752B7')
          label.pack(padx = 3, pady = 3)

root.mainloop()          