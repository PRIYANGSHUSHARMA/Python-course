from tkinter import*



window = Tk()
window.title("Sample Frame")
window.geometry("300x200")

border_effects = [FLAT, SUNKEN, GROOVE, RAISED, RIDGE]
for r in border_effects:
     frame = Frame(master = window, relief = r, borderwidth = 5)
     frame.pack(side = RIGHT)
     label = Label(master=frame, text=r)
     label.pack()

window.mainloop()


