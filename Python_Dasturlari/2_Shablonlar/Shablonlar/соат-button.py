from tkinter import *
import time
def button_clicked():
    # tugma matni
    button['text'] = time.strftime('%H:%M:%S')
root=Tk()
# tugmani yaratamiz
button = Button(root)
# yratilgandan so'ng kofiguratsiysini sozlaymiz
button.configure(text=time.strftime('%H:%M:%S'), command=button_clicked)
# kbadrat qabusni ham ishlatsa bo'ladi:
# button['text'] = time.strftime('%H:%M:%S')
# button['command'] = button_clicked
button.pack()
root.mainloop()