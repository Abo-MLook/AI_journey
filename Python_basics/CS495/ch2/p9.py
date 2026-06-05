from tkinter import *

def change(event):
    label.config(text="Changed Text")

root = Tk()

label = Label(root, text="Click me")
label.pack()

label.bind("<Button>", change)

root.mainloop()