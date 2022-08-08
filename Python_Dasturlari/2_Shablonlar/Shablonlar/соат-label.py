
from tkinter import *
import time
def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')
root=Tk()
label = Label(font='sans 20')
label.pack()
label.after_idle(tick)
root.mainloop()
 
