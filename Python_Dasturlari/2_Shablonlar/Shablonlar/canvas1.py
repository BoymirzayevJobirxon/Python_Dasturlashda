from tkinter import *
     
canvas = Canvas(width=300, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)                
     
canvas.create_oval(10, 10, 200, 200, width=4, fill='blue')
     
     
widget = Label(canvas, text='AAA', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)     
mainloop()
