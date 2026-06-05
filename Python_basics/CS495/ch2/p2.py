from tkinter import *

p_main = Tk()

l1 = Label(p_main,text="Enter something to print in terminal")
l1.pack()

e1 = Entry(p_main)
e1.pack()

def show(): print(e1.get())

b1 = Button(p_main,text="Print",command=show)
b1.pack()
p_main.mainloop()
