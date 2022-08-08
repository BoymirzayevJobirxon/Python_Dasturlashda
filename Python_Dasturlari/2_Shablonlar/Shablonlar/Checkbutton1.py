from tkinter import *      
root = Tk()
states = []                 
for i in range(10):
    var = IntVar()
    chk = Checkbutton(root, text=str(i), variable=var)
    chk.pack(side=LEFT)
    states.append(var)
print (map((lambda var: var.get()), states))
root.mainloop()
#print (map((lambda var: var.get()), states))
