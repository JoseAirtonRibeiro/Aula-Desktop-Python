from tkinter import *
win2 = Tk()
def Placeholder_(event):
    e.config(state=NORMAL)
    e.delete(0, 'end')

e1 = Entry(win2, width=200)
e = Entry(win2, width=200)
e.insert(0, 'enter name')
e.config(state=DISABLED)
e.bind('<Button-1>', Placeholder_)
e.pack()
e1.pack()
win2.mainloop()