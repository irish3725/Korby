#!/usr/bin/python3

import Korby
import tkinter as tk
from tkinter.font import Font
import time
import queue
import Animation
import actions
import sys
import threading
import sock_con

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
                
        self.clear()

                

    def clear(self):
        self.actions.clear()
        self.aButtons.reset()

    def set_direction(self, direction):
        self.direction=direction
 
    def run(self):
        self.win.title("Go Korby!") 
        self.win.geometry("800x500")

        # button to move body
        bodyButton = tk.Button(self.win, height="4", width="7", text="Body", command=lambda: self.add('body'))
        bodyButton.grid(column=0, row=0, pady=5, padx=10)
        self.bRightRadio = tk.Radiobutton(self.win, height="2",text="right", variable=self.radio, value=4, command=lambda: self.set_direction('right'))
        self.bRightRadio.grid(column=0, row=1, pady=0, padx=10)
        self.bLeftRadio = tk.Radiobutton(self.win, height="2", text="left", variable=self.radio, value=5,command=lambda: self.set_direction('left'))
        self.bLeftRadio.grid(column=0, row=2, pady=0, padx=10)

        
        # button to nod head 
        nodButton = tk.Button(self.win, height="4", width="7", text="Head Nod", command=lambda: self.add('head'))
        nodButton.grid(column=1, row=0, pady=5, padx=10) 
        self.upRadio = tk.Radiobutton(self.win, height="2", text="up", variable=self.radio, value=0, command=lambda: self.set_direction('up'))
        self.upRadio.grid(column=1, row=1, pady=0, padx=10)
        self.downRadio = tk.Radiobutton(self.win, height="2", text="down", variable=self.radio, value=1, command=lambda: self.set_direction('down'))
        self.downRadio.grid(column=1, row=2, pady=0, padx=10)
  
        # button to shake head 
        shakeButton = tk.Button(self.win, height="4", width="7", text="Head Shake", command=lambda: self.add('head'))
        shakeButton.grid(column=2, row=0, pady=0, padx=10) 
        self.rightRadio = tk.Radiobutton(self.win, height="2", text="right", variable=self.radio, value=6, command=lambda: self.set_direction('right'))
        self.rightRadio.grid(column=2, row=1, pady=5, padx=10)
        self.leftRadio = tk.Radiobutton(self.win, height="2", text="left", variable=self.radio, value=7, command=lambda: self.set_direction('left'))
        self.leftRadio.grid(column=2, row=2, pady=0, padx=10)

        # button to move wheels
        wheelsButton = tk.Button(self.win, height="4", width="7", text="Wheels", command=lambda: self.add('wheels'))
        wheelsButton.grid(column=3, row=0, pady=5, padx=10) 
        self.forwardRadio = tk.Radiobutton(self.win, height="2", text="forward", variable=self.radio, value=8, command=lambda: self.set_direction('go forward'))
        self.forwardRadio.grid(column=3, row=1, pady=0, padx=10)
        self.backRadio = tk.Radiobutton(self.win, height="2", text="backward", variable=self.radio, value=9, command=lambda: self.set_direction('go back'))
        self.backRadio.grid(column=3, row=2, pady=0, padx=10)


        # button to turn wheels
        turnButton = tk.Button(self.win, height="4", width="7", text="Turn", command=lambda: self.add('wheels'))
        turnButton.grid(column=4, row=0, pady=5, padx=10) 
        self.tRightRadio = tk.Radiobutton(self.win, height="2", text="right", variable=self.radio, value=10, command=lambda: self.set_direction('right'))
        self.tRightRadio.grid(column=4, row=1, pady=0, padx=10)
        self.tLeftRadio = tk.Radiobutton(self.win, height="2", text="left", variable=self.radio, value=11, command=lambda: self.set_direction('left'))
        self.tLeftRadio.grid(column=4, row=2, pady=0, padx=10)


        # duration spin box
        self.Spin = tk.Spinbox(self.win, width="3", from_=0, to=30, increment=0.5, textvariable=self.duration, font=Font(size=36))
        self.Spin.grid(column=5, row=0, pady=10, padx=10)

  
        # button to start
        goButton = tk.Button(self.win, height="2", width="7", text="Go", command=self.go)
        goButton.grid(column=5, row=3, pady=5, padx=10) 

        # button to clear
        clearButton = tk.Button(self.win, height="2", width="7", text="Clear", command=self.clear)
        clearButton.grid(column=5, row=4, pady=5, padx=10) 


        # button to exit
        exitButton = tk.Button(self.win, height="2", width="7", text="Exit", command=sys.exit)
        exitButton.grid(column=5, row=5, pady=5, padx=10) 
 


        frame = tk.Frame(self.win, width=920, height=500, bg="#ffffff")
#        frame.grid(columnspan=4, column=0, row=4, padx=15, pady=10)
#        frame.grid_propagate(False)

        self.win.mainloop()


if __name__ == '__main__':

    gui = GUI()
    server = sock_con.sock_con(gui)

    gui.run()

    # create list of threads
    threads = []

    # create server thread
    threads.append(threading.Thread(name='tcp_server', target=server.listen))

    # start all threads
    for thread in threads:
        thread.start()

    # join all threads
    for thread in threads:
        thread.join()

