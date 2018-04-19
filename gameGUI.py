#!/usr/bin/python3

import Korby
import tkinter as tk
from tkinter.font import Font
import time
import queue
import Animation
import actions
import sys
from final_game import *

class GUI():
    
    def __init__(self):
        # create widow
        self.win = tk.Tk()
        # list of actions for actual movement
        # self.actions = [['animation', '', 0]]
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
 
        self.firstMove = True        
        self.player = player(1)
        self.lastMove = "north"
        self.newMove = ""
        self.gameText = ""
        self.game180 = 3
        self.game90 = 1.5
        self.gameForward = 1

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
        # thread = threading.Thread(name='animate', target=a.update)
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

####################################################################

    def moveNorth(self, nm, running=False):
        self.newMove = nm

        if "dead" in self.gameText:
            pass                
        elif "north" in self.gameText:
            if self.lastMove == "":
                self.lastMove = self.newMove
            
            if self.lastMove == "north":
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "south":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game180))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "east":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "west":
                self.Korb.turnWheels(5000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()

            self.lastMove = self.newMove
        if running == False:
            self.gameText = self.player.action('w')
        self.run(self.gameText)

    
    def moveSouth(self, nm, running=False):
        self.newMove = nm
       
        if "dead" in self.gameText:
            pass
        elif "south" in self.gameText:
            if self.lastMove == self.newMove:
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "north":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game180))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "west":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "east":
                self.Korb.turnWheels(5000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()

            self.lastMove = self.newMove
        if running == False:
            self.gameText = self.player.action('s')
        self.run(self.gameText)


    def moveEast(self, nm, running=False):
        self.newMove = nm

        if "dead" in self.gameText:
            pass
        elif "east" in self.gameText:
            if self.lastMove == "":
                self.lastMove = self.newMove

            if self.lastMove == "east":
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "west":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game180))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "south":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "north":
                self.Korb.turnWheels(5000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()

            self.lastMove = self.newMove
        if running == False:
            self.gameText = self.player.action('d')
        self.run(self.gameText) 


    def moveWest(self, nm, running=False):
        self.newMove = nm

        if "dead" in self.gameText:
            pass
        elif "west" in self.gameText:
            if self.lastMove == "":
                self.lastMove = self.newMove

            if self.lastMove == "west":
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "east":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game180))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "north":
                self.Korb.turnWheels(7000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()
            elif self.lastMove == "south":
                self.Korb.turnWheels(5000)
                time.sleep(float(self.game90))
                self.center()
                self.Korb.moveWheels(5000)
                time.sleep(float(self.gameForward))
                self.center()

            self.lastMove = self.newMove
        if running == False:
            self.gameText = self.player.action('a')
        self.run(self.gameText)
    
    def fight(self, fiteme):
        if "dead" in self.gameText:
            self.gameText = self.player.action('f')
            self.run(self.gameText)
        if "fight" in self.gameText:
            self.Korb.fightArm()
            time.sleep(float(0.7))
            self.gameText = self.player.action('f')
            self.run(self.gameText)
            
    def runAway(self, runme):
        if "dead" in self.gameText:
            pass
        else:
            self.gameText = self.player.action('r')
            self.Korb.runArms()        
        
        if "running north" in self.gameText:
            print("running north")
            self.moveNorth("north", running=True)
        elif "running south" in self.gameText:
            print("running south")
            self.moveSouth("south", running=True)
        elif "running east" in self.gameText:
            print("running east")
            self.moveEast("east", running=True)
        elif "running west" in self.gameText:
            print("running west")
            self.moveWest("west", running=True)
        

####################################################################
 
    def run(self, printText):
        self.win.title("Go Korby!") 
        self.win.geometry("800x500")
        self.center()

        # NORTH 
        northButton = tk.Button(self.win, height="4", width="8", text="North", command=lambda: self.moveNorth("north"))
        northButton.grid(column=2, row=1, pady=5, padx=10) 
  
        # EAST 
        eastButton = tk.Button(self.win, height="4", width="8", text="East", command=lambda: self.moveEast("east"))
        eastButton.grid(column=3, row=2, pady=5, padx=10) 

        # SOUTH
        southButton = tk.Button(self.win, height="4", width="8", text="South", command=lambda: self.moveSouth("south"))
        southButton.grid(column=2, row=3, pady=5, padx=10) 

        # WEST
        westButton = tk.Button(self.win, height="4", width="8", text="West", command=lambda: self.moveWest("west"))
        westButton.grid(column=1, row=2, pady=5, padx=10)

        # FIGHT
        fightButton = tk.Button(self.win, height="4", width="8", text="FIGHT", command=lambda: self.fight("fight"))
        fightButton.grid(column=4, row=1, pady=5, padx=10)
        
        # RUN
        runButton = tk.Button(self.win, height="4", width="8", text="RUN", command=lambda: self.runAway("run"))
        runButton.grid(column=4, row=2, pady=5, padx=10)

        # TEXT
        if self.firstMove:
            self.firstMove = False
            self.gameText = self.player.action('start')
            textField = tk.Label(self.win, height="13", width="45", text=self.gameText)
        else:
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
    gui = GUI()
    gui.run("")
