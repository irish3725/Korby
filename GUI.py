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
        # radio button variable
        self.radio = 0
        # variable for storing duration
        self.duration = 1
 
    def center(self):
        self.Korb.reset()

    def moveHead(self): 
        duration = self.duration 
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
        print('movement up =', self.h_up)
        print('duration =', self.Spin.get())
        print('adding head move')
        self.q.put('head')

    def go(self):
        # create a place for kirby animation
        self.top = tk.Toplevel()
        self.anime = Animation.Animation(self.top)
        self.anime.update(0)
        while not self.q.empty():
            current = self.q.get()
            if current == 'head':
                self.moveHead()
                time.sleep(2)
        #self.anime.stop()
 
    def run(self):
        self.win.title("Go Korby!")

        self.win.geometry("800x500")

        # button to move back to center
        bodyButton = tk.Button(self.win, height="4", width="10", text="Body", command=self.center)
        bodyButton.grid(column=0, row=0, pady=10, padx=10)
        self.bRightRadio = tk.Radiobutton(self.win, text="right", variable=self.radio, value=4)
        self.bRightRadio.grid(column=0, row=1, pady=0, padx=10)
        self.bLeftRadio = tk.Radiobutton(self.win, text="left", variable=self.radio, value=5)
        self.bLeftRadio.grid(column=0, row=2, pady=0, padx=10)

        
        # button to move head 
        nodButton = tk.Button(self.win, height="4", width="10", text="Head Nod", command=self.addHead)
        nodButton.grid(column=1, row=0, pady=0, padx=10) 
        self.upRadio = tk.Radiobutton(self.win, text="up", variable=self.radio, value=0)
        self.upRadio.grid(column=1, row=1, pady=0, padx=10)
        self.downRadio = tk.Radiobutton(self.win, text="down", variable=self.radio, value=1)
        self.downRadio.grid(column=1, row=2, pady=0, padx=10)
  
        # button to move head 
        shakeButton = tk.Button(self.win, height="4", width="10", text="Head Shake", command=self.addHead)
        shakeButton.grid(column=2, row=0, pady=0, padx=10) 
        self.rightRadio = tk.Radiobutton(self.win, text="right", variable=self.radio, value=2)
        self.rightRadio.grid(column=2, row=1, pady=0, padx=10)
        self.leftRadio = tk.Radiobutton(self.win, text="left", variable=self.radio, value=3)
        self.leftRadio.grid(column=2, row=2, pady=0, padx=10)

        # button to move wheels
        wheelsButton = tk.Button(self.win, height="4", width="10", text="Wheels", command=self.moveWheels)
        wheelsButton.grid(column=3, row=0, pady=10, padx=10) 
        self.forwardRadio = tk.Radiobutton(self.win, text="forward", variable=self.radio, value=2)
        self.forwardRadio.grid(column=3, row=1, pady=0, padx=10)
        self.backRadio = tk.Radiobutton(self.win, text="backward", variable=self.radio, value=3)
        self.backRadio.grid(column=3, row=2, pady=0, padx=10)


        # button to move wheels
        turnButton = tk.Button(self.win, height="4", width="10", text="Turn", command=self.moveWheels)
        turnButton.grid(column=4, row=0, pady=10, padx=10) 
        self.tRightRadio = tk.Radiobutton(self.win, text="right", variable=self.radio, value=2)
        self.tRightRadio.grid(column=4, row=1, pady=0, padx=10)
        self.tLeftRadio = tk.Radiobutton(self.win, text="left", variable=self.radio, value=3)
        self.tLeftRadio.grid(column=4, row=2, pady=0, padx=10)


        # duration spin box
        self.Spin = tk.Spinbox(self.win, width="10", from_=0, to=30, increment=0.5, textvariable=self.duration)
        self.Spin.grid(column=6, row=0, pady=10, padx=10)

  
        # button to move wheels
        goButton = tk.Button(self.win, height="4", width="10", text="Go", command=self.go)
        goButton.grid(column=6, row=3, pady=10, padx=10) 

        # button to move wheels
        exitButton = tk.Button(self.win, height="4", width="10", text="Exit", command=sys.exit)
        exitButton.grid(column=6, row=4, pady=10, padx=10) 
 


        frame = tk.Frame(self.win, width=920, height=500, bg="#ffffff")
#        frame.grid(columnspan=4, column=0, row=4, padx=15, pady=10)
#        frame.grid_propagate(False)

        self.win.mainloop()


if __name__ == '__main__':

    gui = GUI()
    gui.run() 



