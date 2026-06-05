from tkinter import *

def click(event):
    print("Single click")

def double(event):
    print("Double click")

root = Tk()

btn = Button(root, text="Press Me")
btn.pack()

btn.bind("<Button-1>", click)
btn.bind("<Double-1>", double)

root.mainloop()