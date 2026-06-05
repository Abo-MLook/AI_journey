from tkinter import *

p_main = Tk()

l1 = Label(p_main,text="Enter something to print in terminal")
l1.grid(row=0,column=0)

e1 = Entry(p_main)
e1.grid(row=0,column=1)
def show(): print(e1.get())
b1 = Button(p_main,text="Print",command=show)
b1.grid(row=1)

p_main.mainloop()



