#!/usr/bin/python3

import sys
import Korby
import tkinter as tk
import time
import queue

class GUI():
    
    def __init__(self):
        self.win = tk.Tk()
        self.Korb = Korby.Korby(self.win)
        # load background image
        self.bg_img = tk.PhotoImage(file='korby_face_smaller.gif')
        self.bg_label = tk.Label(self.win, image=self.bg_img)
        # place background image
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
 

    def go(self):
        print('go')    
 
    def moveHead(self, direction, time):
        self.Korb.moveHeadU()
      
    def center(self):
        self.Korb.reset()
 
    def run(self):
        self.win.title("It's just a drill")

        self.win.geometry("800x500")

        headButton = tk.Button(self.win, width="20", text="Drill", command=self.Korb.moveHeadU)
        headButton.grid(column=0, row=0, pady=10, padx=10)

        centerButton = tk.Button(self.win, width="20", text="Center", command=self.center)
        centerButton.grid(column=1, row=0, pady=10, padx=10)
       
        
 

#        frame = tk.Frame(self.win, width=920, height=500)
#        frame.grid(columnspan=4, row=4, padx=15, pady=10)
#        frame.grid_propagate(False)

        self.win.mainloop()


if __name__ == '__main__':

    gui = GUI()

    if len(sys.argv) == 1:
        gui.center()        

    if len(sys.argv) > 1:
        gui.run() 



