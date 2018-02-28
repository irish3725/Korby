#!/usr/bin/python3

import sys
import Korby
import tkinter as tk
import time
import queue
import Animation

class GUI():
    
    def __init__(self):
        self.q = queue.Queue()
        # create widow
        self.win = tk.Tk()
        # create Korby object for moving robot
        self.Korb = Korby.Korby(self.win)
        # load background image
        self.bg_img = tk.PhotoImage(file='korby_face.gif')
        self.bg_label = tk.Label(self.win, image=self.bg_img)
        # place background image
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # variable for up/down head position
        self.h_up = 6000
        # variable for lateral head position
        self.h_lat = 6000
        # variable for body position
        self.body = 6000
        # varable for forward/back wheels
        self.wheels = 6000
        # variable for turn wheels
        self.turn = 6000
        # variable for storing duration
        self.duration = 1
 
    def center(self):
        self.Korb.reset()

    def moveHead(self): 
        duration = 3 
        self.h_lat +=3000
        self.Korb.moveHead(self.h_lat)
        time.sleep(duration)
        self.center()
    
    def moveWheels(self):
        duration = 1
        # set wheels to 1000 less
        self.wheels -= 1000 
        self.Korb.moveWheels(self.wheels)
        time.sleep(duration)
        self.center()

    def addHead(self):
        print('adding head move')
        self.q.put('head')

    def go(self):
        a = Animation.Animation()
        a.update(0)
        while not self.q.empty():
            current = self.q.get()
            if current == 'head':
                self.moveHead()
                time.sleep(2)
        a.stop()
 
    def run(self):
        self.win.title("It's just a drill")

        self.win.geometry("800x500")

        # button to move back to center
        centerButton = tk.Button(self.win, height="4", width="10", text="Body", command=self.center)
        centerButton.grid(column=0, row=0, pady=10, padx=10)
     
        # button to move head 
        headButton = tk.Button(self.win, height="4", width="10", text="Head", command=self.addHead)
        headButton.grid(column=1, row=0, pady=0, padx=10) 
        self.headSpin = tk.Spinbox(self.win, width="5", from_=0, to=30, increment=0.5, textvariable=self.duration)
        self.headSpin.grid(column=1, row=1, pady=10, padx=10)

        # button to move wheels
        wheelsButton = tk.Button(self.win, height="4", width="10", text="Wheels", command=self.moveWheels)
        wheelsButton.grid(column=2, row=0, pady=10, padx=10) 

        # button to move wheels
        turnButton = tk.Button(self.win, height="4", width="10", text="Turn", command=self.moveWheels)
        turnButton.grid(column=3, row=0, pady=10, padx=10) 
  
        # button to move wheels
        goButton = tk.Button(self.win, height="4", width="10", text="Go", command=self.go)
        goButton.grid(column=0, row=3, pady=10, padx=10) 

        # button to move wheels
        exitButton = tk.Button(self.win, height="4", width="10", text="Exit", command=sys.exit)
        exitButton.grid(column=6, row=3, pady=10, padx=10) 
 


        frame = tk.Frame(self.win, width=920, height=500, bg="#ffffff")
#        frame.grid(columnspan=4, column=0, row=4, padx=15, pady=10)
#        frame.grid_propagate(False)

        self.win.mainloop()


if __name__ == '__main__':

    gui = GUI()
    gui.run() 



