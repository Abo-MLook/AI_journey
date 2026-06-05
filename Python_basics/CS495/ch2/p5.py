from tkinter import *

root = Tk()

l = Listbox(root)

l.insert(END, "Python")
l.insert(END, "Java")

l.pack()

def show():
    print(l.get(ACTIVE))

b = Button(root, text="Show", command=show)
b.pack()

root.mainloop()