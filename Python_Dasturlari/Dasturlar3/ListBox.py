from tkinter import *
root = Tk()

scrollbar = Scrollbar(root, orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM, fill=X)

mylist = Listbox(root, xscrollcommand=scrollbar.set)
for line in range(100):
    msg = "number is " + str(line)
    mylist.insert(END, msg)
mylist.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=mylist.xview)
mainloop()
