from tkinter import *
import time
import os
import sys

root = Tk()

frames = [PhotoImage(file='kirbywalk.gif',format = 'gif -index %i' %(i)) for i in range(10)]

def update(ind):
    if ind < 10:
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(100, update, ind)
    elif ind == 10:
        ind = 0
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(100, update, ind)
        
def stop():
        label.forget()
       
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
