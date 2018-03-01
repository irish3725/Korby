#!/usr/bin/python3

import tkinter as tk
import GUI

class Actions:

    def __init__(self, win, gui):
        # get main tk window
        self.win = win
        # get gui to delete commands
        self.gui = gui
        # list of buttons to be displayed
        self.buttons = []
        # list of commands
        self.commands = []
    
    ## redraws all buttons onto screen
    def reDraw(self):
        # for each button in list
        for command in self.commands:
            index = len(self.buttons)
            # create string to be written to the button 
            buttonText = str(command[0]) + '\n' + str(command[1]) + '\n' + str(command[2])
            # create new button
            button = tk.Button(self.win, height="4", width="7", text=buttonText, command=lambda: self.delButton(index))
            # add button to list of buttons
            self.buttons.append(button)
            # get the index of that button for drawing at coordinate
            cl = (len(self.buttons) - 1) % 5 
            rw = int((len(self.buttons) - 1) / 5) + 6
            # draw button in row 6 at index index
            button.grid(column=cl, row=rw, pady=3, padx=10)


    ## adds a single button
    def addButton(self, entry): # clear screen of buttons
        self.clear()
        # append the new command to the list of commands
        self.commands.append(entry)
        # redraw the buttons
        self.reDraw()
    
    ## deletes a single button
    def delButton(self, index):
        index = len(self.buttons) - 1
        # clear the screen of buttons
        self.clear()
        # remove button from list of buttons
        self.commands.pop(index)
        self.gui.actions.pop(index)
        # draw all buttons on screen
        self.reDraw()

    ## clears the screen and emptys our list of buttons
    def reset(self):
        # clear screen
        self.clear()
        # empty list of buttons
        self.buttons.clear()
        # clear commans
        self.commands.clear()

    ## deletes all buttons from the screen
    def clear(self):
        # for all buttons in list
        for button in self.buttons:
            # remove button from screen
            button.destroy()

        self.buttons.clear()

#            button.forget()
