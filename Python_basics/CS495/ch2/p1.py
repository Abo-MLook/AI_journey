from tkinter import *

def hello():
    print("hello")

top = Tk()
l1 = Label(top,text="Hello world")
l1.pack()
b1 = Button(top,text="here",command=hello)
b1.pack()
top.mainloop()

