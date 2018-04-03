#!/usr/bin/python3

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
        print('resetting all')
        self.x.setTarget(0, 6000)
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)
        self.x.setTarget(3, 6000)
        self.x.setTarget(4, 6000)


    ## set body, head, wheels to middle/not moving
    def middle(self, key):
        self.x.setTarget(0, 6000)
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)
        self.x.setTarget(3, 6000)
        self.x.setTarget(4, 6000)

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
