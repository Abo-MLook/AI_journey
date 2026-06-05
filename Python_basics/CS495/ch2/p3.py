from tkinter import *

p_main = Tk()

l1 = Label(p_main,text="Enter something to print in terminal")
l1.pack()
#============================
v1 =IntVar()
v2 =IntVar()
c1 = Checkbutton(p_main,text="python",variable=v1)
c2 = Checkbutton(p_main,text="java",variable=v2)
c1.pack()
c2.pack()
#============================
v = IntVar()

r1 = Radiobutton(p_main, text="Python", variable=v, value=1)
r2 = Radiobutton(p_main, text="Java", variable=v, value=2)
r1.pack()
r2.pack()
#============================
lis = Listbox(p_main)
lis.insert(END,"python")
lis.insert(END,"java")
lis.insert(END,"c")

lis.pack()


p_main.mainloop()
