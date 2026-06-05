from tkinter import *
top = Tk()
def display(c):
    if c == 1:
        print('Check box 1 value :',v1.get())
    elif c == 2:
        print('Check box 2 value :', v2.get())
v1 = IntVar()
v2 = IntVar()
cb1 = Checkbutton(top, text='python', variable=v1,onvalue=1,offvalue=0,command= lambda:
display(1))
cb1.grid(row=2,column=2)
cb2 = Checkbutton(top, text='java', variable=v2,onvalue=1,offvalue=0,command= lambda:
display(2))
cb2.grid(row=3,column=2)
v1.set(True) # this will set (check) the checkbutton cb1 initially
top.mainloop()
