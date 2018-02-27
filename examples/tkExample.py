import tkinter as tk


def fun():
    print("Button is pushed")
    
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return   
def mouseClick(event):
    print(event)
def arrow(key):
    #print("Arrow up")
    print(key)
    if key.keycode==39:
        print("Right")
        
win = tk.Tk()
win.bind('<Up>', arrow)
win.bind('<Left>', arrow)
win.bind('<Down>', arrow)
win.bind('<Right>', arrow)
win.bind('<Button>', mouseClick)

myCan = tk.Canvas(win, bg="#333333", width="500", height="500")
myCan.bind('<Motion>', motion)

myCan.pack()

lab = tk.Label(win, text="Hello Tkinter!")

lab.pack()

button = tk.Button(win, width="15", text="print", bg="blue", fg="yellow", command=fun)
button.pack(side = tk.RIGHT)
button2 = tk.Button(win, width="15", text="Second", bg="blue", fg="yellow", command=fun)
button2.pack(side = tk.BOTTOM)

win.mainloop()
