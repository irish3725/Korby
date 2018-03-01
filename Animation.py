from tkinter import *
import time
import os
import sys

class Animation():

    def __init__(self, top):
        self.root = top
        self.frames = [PhotoImage(file='kirbywalk.gif',format = 'gif -index %i' %(i)) for i in range(10)]
        self.frame = self.frames[0]
        self.label = Label(self.root)
        self.label.pack()

    def update(self, ind):
        if ind < 10:
            self.frame = self.frames[ind]
            ind += 1
            self.label.configure(image=self.frame)
            self.root.after(100, self.update, ind)
        elif ind == 10:
            ind = 0
            self.frame = self.frames[ind]
            ind += 1
            self.label.configure(image=self.frame)
            self.root.after(100, self.update, ind)
            
    def stop(self):
            sys.exit()

    def run(self):
        print('running animation')
        self.root.after(0, self.update, 0)
        self.root.mainloop()
    

if __name__ == '__main__':           
    root = Tk()
    a = Animation(root)
    a.run()
