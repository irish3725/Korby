#!/usr/bin/python3

import tkinter as tk
import time
import queue

class Button():

    def makeDrill():
        print("boop")
#        instance = tk.Button(frame, text='Move', width=25, height=10, command=m.popUp)
#        Button.place(instance)

if __name__ == '__main__':
    
    win = tk.Tk()
    win.title("It's just a drill")

    drillButton = tk.Button(win, width="20", text="Drill", command=Button.makeDrill)
    drillButton.grid(column=0, row=0, pady=10)

    frame = tk.Frame(win, width=920, height=500)
    frame.grid(columnspan=4, row=1, padx=15, pady=10)
#    frame.grid_propagate(False)

    win.mainloop()




