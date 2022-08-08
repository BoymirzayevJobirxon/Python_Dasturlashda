from tkinter import *      
root = Tk()                   
     
def radio1():                  
    tmp = IntVar()
    for i in range(10): 
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)    
     
radio1()
root.mainloop()
