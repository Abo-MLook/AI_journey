from tkinter import *
top = Tk()
def display():
    print('the value associated to the selected radio button: ',v1.get())
v1 = IntVar() # We used control variable here
r1 = Radiobutton(top, text='python', variable=v1, value=1,command=display)
r1.grid(row=1,column=1)
r2 = Radiobutton(top, text='java', variable=v1, value=0,command=display)
r2.grid(row=1,column=2)
r3 = Radiobutton(top, text='C++', variable=v1, value=4,command=display)
r3.grid(row=1,column=3)
v1.set(4) # this will set (check) the radiobutton r3 initially
top.mainloop()