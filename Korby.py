#!/usr/bin/python3

import time
import sys
import tkinter as tk
from Maestro import Controller


## Korby is the name of our robot!
class Korby():

    ## initialize a Korby object with an instance of the Maestro controller
    ## init to work with cam's code
    def __init__(self, win):
    ## init to work with alex's code
#    def __init__(self):
        self.root = win
        self.x = Controller()

    ## set body, head, wheels to middle/not moving
    def reset(self):
        self.x.setTarget(0, 6000)
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)
        self.x.setTarget(3, 6000)
        self.x.setTarget(4, 6000)

        self.x.setTarget(6, 4500) #right shoulder up and down
        self.x.setTarget(7, 7000) #right shoulder in and out
        self.x.setTarget(8, 5000) #right elbow
        self.x.setTarget(9, 4500) #right wrist up and down
        self.x.setTarget(10, 6000) #right wrist left and right
        self.x.setTarget(11, 1000) #right hand open and close

        self.x.setTarget(12, 5500) #left shoulder up and down
        self.x.setTarget(13, 7500) #left shoulder in and out
        self.x.setTarget(14, 6000) #left elbow
        self.x.setTarget(15, 5500) #left wrist up and down
        self.x.setTarget(16, 6000) #left wrist left and right
        self.x.setTarget(17, 6000) #left hand open and close

    def runArms(self):
        self.x.setTarget(6, 9000)
        self.x.setTarget(8, 9000)
        time.sleep(float(1))
        self.x.setTarget(10, 8000)
        time.sleep(float(0.5))
        self.x.setTarget(10, 4000)
        time.sleep(float(0.5))
        self.x.setTarget(10, 6000)
        time.sleep(float(0.7))
        self.reset() 

    def fightArm(self):
        #self.x.setTarget(0, 4000)
        #self.x.setTarget(3, 7000)        

        self.x.setAccel(6, 5)
        self.x.setAccel(7, 5)
        self.x.setAccel(8, 5)

        self.x.setTarget(6, 9000)
        self.x.setTarget(8, 9000)
        self.x.setTarget(7, 9000)

        time.sleep(float(1.3))

        self.x.setAccel(6, 255)
        self.x.setAccel(7, 255)
        self.x.setAccel(8, 255)

        time.sleep(float(0.5))

        self.x.setTarget(7, 7000)
        self.x.setTarget(8, 4000)
        time.sleep(float(0.1))
        self.x.setTarget(6, 8000)

    ## set body, head, wheels to middle/not moving
    def middle(self, key):
        self.x.setTarget(0, 6000)
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)
        self.x.setTarget(3, 6000)
        self.x.setTarget(4, 6000)

        self.x.setTarget(6, 4500) #right shoulder up and down
        self.x.setTarget(7, 7000) #right shoulder in and out
        self.x.setTarget(8, 7000) #right elbow
        self.x.setTarget(9, 4500) #right wrist up and down
        self.x.setTarget(10, 6000) #right wrist left and right
        self.x.setTarget(11, 6000) #right hand open and close

        self.x.setTarget(12, 5500) #left shoulder up and down
        self.x.setTarget(13, 7500) #left shoulder in and out
        self.x.setTarget(14, 4000) #left elbow
        self.x.setTarget(15, 5500) #left wrist up and down
        self.x.setTarget(16, 6000) #left wrist left and right
        self.x.setTarget(17, 6000) #left hand open and close

    ## move body to the left a little
    def moveBodyLeft(self, key):
        change = 900
        position = x.getPosition(0)
        if position < 8000:
            self.x.setTarget(0, position + change)    

    ## move body to the right a little
    def moveBodyRight(self, key):
        change = 900
        position = self.x.getPosition(0)
        if position > 3000:
            self.x.setTarget(0, position - change)    

    def moveBody(self, position):
        print('body at Korb position is', position)
        self.x.setTarget(0, position)    

    def nodHead(self, position):
        self.x.setTarget(4, position)
        
    def turnHead(self, position):
        self.x.setTarget(3, position)

    ## move head to the right a little
    def moveHeadRight(self, key):
        change = 900
        position = self.x.getPosition(3)
        if position > 2500:
            self.x.setTarget(3, position - change)

    ## move head to the left a little
    def moveHeadLeft(self, key):
        change = 900
        position = self.x.getPosition(3)
        if position < 8000:
            self.x.setTarget(3, position + change)

    ## move head up a little
    def moveHeadUp(self, key):
        change = 900    
        position = self.x.getPosition(4)
        if position < 8000:
            self.x.setTarget(4, position + change)

    ## move head down a little
    def moveHeadDown(self, key):
        change = 900    
        position = self.x.getPosition(4)
        if position > 2800:
            self.x.setTarget(4, position - change)

    def moveWheels(self, speed):
        self.x.setTarget(1, speed)

    def turnWheels(self, speed):
        self.x.setTarget(2, speed)

    ## change wheels to move forward faster
    def moveForward(self, key):
        change = 300
        position = self.x.getPosition(1)
        if position > 4800:
            self.x.setTarget(1, position - change)

    ## change wheels to move backward faster
    def moveBackward(self, key):
        change = 300
        position = self.x.getPosition(1)
        if position < 7200:
            self.x.setTarget(1, position + change)

    ## change wheels to turn left
    def turnLeft(self, key):
        position = self.x.getPosition(2)
        if position == 6000:
            self.x.setTarget(2, 7000)
        elif position == 5000:
            self.x.setTarget(2, 6000)

    ## change wheels to turn right
    def turnRight(self, key):
        position = self.x.getPosition(2)
        if position == 6000:
            self.x.setTarget(2, 5000)    
        elif position == 7000:
            self.x.setTarget(2, 6000)

    ## stop wheels
    def stop(self, key):
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)
    
    def endProgram(self, key):
        sys.exit()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        Korb = Korby()


    if len(sys.argv) < 2:
        win = tk.Tk()
        Korb = Korby(win)
        Korb.middle
             
        win.bind('<q>', Korb.endProgram)
        win.bind('<n>', Korb.stop)
        win.bind('<m>', Korb.middle)

        win.bind('<w>', Korb.moveHeadUp) 
        win.bind('<a>', Korb.moveHeadLeft)
        win.bind('<s>', Korb.moveHeadDown)
        win.bind('<d>', Korb.moveHeadRight)

        win.bind('<z>', Korb.moveBodyLeft)
        win.bind('<x>', Korb.moveBodyRight)

        win.bind('<Up>', Korb.moveForward)
        win.bind('<Left>', Korb.turnLeft)
        win.bind('<Right>', Korb.turnRight)
        win.bind('<Down>', Korb.moveBackward)

        win.mainloop()

        #        self.stdscr = curses.initscr()
            
        #        curses.cbreak()
        #        self.stdscr.keypad(1)
        #
        #        # start screen with "press 'q' to quit' written on first line at 10th char
        #        self.stdscr.addstr(1, 10, "press 'q' to quit")
        #        self.stdscr.refresh()
        #
        #        key = ''
        #        # listen for input till we see a q
        #        while key != ord('q'):
        #            key = self.stdscr.getch()
        #            self.stdscr.addch(20,25,key)
        #            self.stdscr.refresh()
        #
        #            # see up pressed
        #            if key == curses.KEY_UP:
        #                self.Korb.moveForward()
        #
        #            # see down pressed
        #            elif key == curses.KEY_DOWN:
        #                self.Korb.moveBackward()
        #
        #            # see left pressed
        #            elif key == curses.KEY_LEFT:
        #                self.Korb.turnLeft()
        #
        #           # see right pressed
        #            elif key == curses.KEY_RIGHT:
        #                self.Korb.turnRight()
        # 
        #            # see a pressed
        #            elif key == ord('a'):
        #                self.Korb.moveHeadLeft()
        #            
        #            # see s pressed
        #            elif key == ord('s'):
        #                self.Korb.moveHeadDown()
        #
        #            # see d pressed
        #            elif key == ord('d'):
        #                self.Korb.moveHeadRight()
        #
        #            # see w pressed
        #            elif key == ord('w'):
        #                self.Korb.moveHeadUp()
        #
        #            # see q pressed
        #            elif key == ord('q'):
        #                self.middle() 
        #
        #            # see z pressed
        #            elif key == ord('z'):
        #                self.Korb.oveBodyLeft()
        #
        #            # see x pressed
        #            elif key == ord('x'):
        #                self.Korb.moveBodyRight()
        #
        #            # see m pressed
        #            elif key == ord('m'):
        #                self.Korb.middle()
        #
        #            # see n pressed
        #            elif key == ord('n'):
        #                self.middle()
