#!/usr/bin/python3

import Korby
import tkinter as tk
from tkinter.font import Font
import time
import queue
import Animation
import actions
import sys
import game

class GUI():
    
    def __init__(self):
        # create widow
        self.win = tk.Tk()
        # list of actions for actual movement
#        self.actions = [['animation', '', 0]]
        self.actions = []
        # actual action buttons for placing on the screen
        self.aButtons = actions.Actions(self.win, self)
        # create Korby object for moving robot
        self.Korb = Korby.Korby(self.win)
        # load background image
        self.bg_img = tk.PhotoImage(file='korby_face.gif')
        self.bg_label = tk.Label(self.win, image=self.bg_img)
        # place background image
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # radio button variable
        self.radio = 0 
        # direction for things
        self.direction = 'up'
        # variable for storing duration
        self.duration = 1 

        self.player = player

    def center(self):
        self.Korb.reset()
 
    def moveBody(self, direction, duration):
        if direction == 'right': #right
            self.Korb.moveBody(4500)
            time.sleep(float(duration))
            self.center()
        elif direction == 'left': #left
            self.Korb.moveBody(7500)
            time.sleep(float(duration))
            self.center() 
        
    def moveHead(self, direction, duration): 
        if direction == 'up': #up
            self.Korb.nodHead(7000)
            time.sleep(float(duration))
            self.center()
        elif direction == 'down': #down
            self.Korb.nodHead(5000)
            time.sleep(float(duration))
            self.center()
        elif direction == 'right': #right
            self.Korb.turnHead(5000)
            time.sleep(float(duration))
            self.center()
        elif direction == 'left': #left
            self.Korb.turnHead(7000)
            time.sleep(float(duration))
            self.center() 
    
    def moveWheels(self, direction, duration):
        if direction == 'go forward': #forward 
            self.Korb.moveWheels(5000)
            time.sleep(float(duration))
            self.center()
        elif direction == 'go back': #back
            self.Korb.moveWheels(7000)
            time.sleep(float(duration))
            self.center()
        elif direction == 'right': #right
            self.Korb.turnWheels(5100)
            time.sleep(float(duration))
            self.center()
        elif direction == 'left': #left 
            self.Korb.turnWheels(7000)
            time.sleep(float(duration))
            self.center()

    def add(self, name, direction=-1, time=-1):
        if len(self.actions) < 11: 
            # if no input for direction or time
            if direction == -1 and time == -1:
                #!!!! WARNING: Don't look directly at the below if statement !!!!#
                if (name == 'head' and self.direction != 'go forward' and self.direction != 'go back') or (name == 'wheels' and self.direction != 'up' and self.direction != 'down') or (name == 'body' and (self.direction == 'right' or self.direction == 'left')): 

                    action = [name, self.direction, self.Spin.get()]
            else:
                action = [name, direction, time]

            # add button to screen
            self.actions.append(action)
            self.aButtons.addButton(action)

    def go(self):
        self.actions.append(['end', '', 0])
        # create a place for kirby animation
        self.top = tk.Toplevel()
        a = Animation.Animation(self.top)
#        thread = threading.Thread(name='animate', target=a.update)
        a.update(0)
        while len(self.actions) > 0:
            current = self.actions[0][0]
            print('current =', current)
            direction = self.actions[0][1]
            duration = self.actions[0][2]
            self.actions.pop(0)
            if current == 'head':
                self.moveHead(direction, duration)
            elif current == 'body':
                self.moveBody(direction, duration)
            elif current == 'wheels':
                self.moveWheels(direction, duration)
            #elif current == 'animation':
            #    self.top = tk.Toplevel()
            #    a = Animation.Animation(self.top)
            #    a.update(0)
            time.sleep(float(duration))
                
        a.stop()
        self.clear()
        return


    def clear(self):
        self.actions.clear()
        self.aButtons.reset()

    def set_direction(self, direction):
        self.direction=direction
 
    def run(self, printText):
        self.win.title("Go Korby!") 
        self.win.geometry("800x500")


        # NORTH 
        northButton = tk.Button(self.win, height="4", width="8", text="North", command=lambda: self.player.action(self.player, 'w'))
        northButton.grid(column=2, row=1, pady=5, padx=10) 
  
        # EAST 
        eastButton = tk.Button(self.win, height="4", width="8", text="East", command=lambda: self.player.action(self.player, 'd'))
        eastButton.grid(column=3, row=2, pady=5, padx=10) 

        # SOUTH
        southButton = tk.Button(self.win, height="4", width="8", text="South", command=lambda: self.player.action(self.player, 's'))
        southButton.grid(column=2, row=3, pady=5, padx=10) 

        # WEST
        westButton = tk.Button(self.win, height="4", width="8", text="West", command=lambda: self.player.action(self.player, 'a'))
        westButton.grid(column=1, row=2, pady=5, padx=10)

        # FIGHT
        fightButton = tk.Button(self.win, height="4", width="8", text="FIGHT", command=lambda: self.player.action(self.player, 'f'))
        fightButton.grid(column=4, row=1, pady=5, padx=10)
        
        # RUN
        runButton = tk.Button(self.win, height="4", width="8", text="RUN", command=lambda: self.player.action(self.player, 'r'))
        runButton.grid(column=4, row=2, pady=5, padx=10)

        # TEXT
        textField = tk.Label(self.win, height="13", width="45", text=printText)
        textField.configure(background="black", foreground="white")
        textField.grid(column=5, row=5, pady=5, padx=10)

        # EXIT
        exitButton = tk.Button(self.win, height="4", width="8", text="Exit", command=sys.exit)
        exitButton.grid(column=1, row=5, pady=5, padx=10) 
 


        frame = tk.Frame(self.win, width=920, height=500, bg="#ffffff")
#        frame.grid(columnspan=4, column=0, row=4, padx=15, pady=10)
#        frame.grid_propagate(False)

        self.win.mainloop()


if __name__ == '__main__':

    print("started main")

    
    gui = GUI()
    gui.run("Welcome to the game. \n Which direction would you like to go?")
