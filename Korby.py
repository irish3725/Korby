#!/usr/bin/python3

import curses
import serial
from sys import version_info
import Maestro


## Korby is our robot!
class Korby():

    def __init__(self):
        self.x = Maestro.Controller()

    ## set body, head, wheels to middle/not moving
    def middle(self):
        self.x.setTarget(0, 6000)
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)
        self.x.setTarget(3, 6000)
        self.x.setTarget(4, 6000)

    ## move body to the left a little
    def moveBodyLeft(self):
        change = 900
        position = x.getPosition(0)
        if position < 8000:
            self.x.setTarget(0, position + change)    

    ## move body to the right a little
    def moveBodyRight(self):
        change = 900
        position = self.x.getPosition(0)
        if position > 3000:
            self.x.setTarget(0, position - change)    

    ## move head to the right a little
    def moveHeadRight(self):
        change = 900
        position = self.x.getPosition(3)
        if position > 2500:
            self.x.setTarget(3, position - change)

    ## move head to the left a little
    def moveHeadLeft(self):
        change = 900
        position = self.x.getPosition(3)
        if position < 8000:
            self.x.setTarget(3, position + change)

    ## move head up a little
    def moveHeadUp(self):
        change = 900    
        position = self.x.getPosition(4)
        if position < 8000:
            self.x.setTarget(4, position + change)

    ## move head down a little
    def moveHeadDown(self):
        change = 900    
        position = self.x.getPosition(4)
        if position > 2800:
            self.x.setTarget(4, position - change)

    ## change wheels to move forward faster
    def moveForward(self):
        change = 300
        position = self.x.getPosition(1)
        if position > 4800:
            self.x.setTarget(1, position - change)

    ## change wheels to move backward faster
    def moveBackward(self):
        change = 300
        position = self.x.getPosition(1)
        if position < 7200:
            self.x.setTarget(1, position + change)

    ## change wheels to turn left
    def turnLeft(self):
        position = self.x.getPosition(2)
        if position == 6000:
            self.x.setTarget(2, 7000)
        elif position == 5000:
            self.x.setTarget(2, 6000)

    ## change wheels to turn right
    def turnRight(self):
        position = self.x.getPosition(2)
        if position == 6000:
            self.x.setTarget(2, 5000)    
        elif position == 7000:
            self.x.setTarget(2, 6000)

    ## stop wheels
    def stop(self):
        self.x.setTarget(1, 6000)
        self.x.setTarget(2, 6000)

class KInterface():

    def __init__(self, Korb):
        self.Korb = Korb 
        self.stdscr = curses.initscr()

    def run(self):
        print("made it into the run function")
        curses.cbreak()
        self.stdscr.keypad(1)

        # start screen with "press 'q' to quit' written on first line at 10th char
        self.stdscr.addstr(1, 10, "press 'q' to quit")
        self.stdscr.refresh()

        key = ''
        while key != ord('q'):
            key = self.stdscr.getch()
            self.stdscr.addch(20,25,key)
            self.stdscr.refresh()

            if key == curses.KEY_UP:
                self.Korb.moveForward()

            elif key == curses.KEY_DOWN:
                self.Korb.moveBackward()

            elif key == curses.KEY_LEFT:
                self.Korb.turnLeft()

            elif key == curses.KEY_RIGHT:
                self.Korb.turnRight()

            elif key == ord('a'):
                self.Korb.moveHeadLeft()
            
            elif key == ord('s'):
                self.Korb.moveHeadDown()

            elif key == ord('d'):
                self.Korb.moveHeadRight()

            elif key == ord('w'):
                self.Korb.moveHeadUp()

            elif key == ord('q'):
                self.middle() 

            elif key == ord('z'):
                self.Korb.oveBodyLeft()

            elif key == ord('x'):
                self.Korb.moveBodyRight()

            elif key == ord('m'):
                self.Korb.middle()

            elif key == ord('n'):
                self.middle()

if __name__ == '__main__':

    Korb = Korby()
    Iface = KInterface(Korb)
    Iface.run()
