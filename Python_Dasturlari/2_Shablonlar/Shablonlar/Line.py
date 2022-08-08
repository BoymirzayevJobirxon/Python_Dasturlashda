from tkinter import *
     
canvas = Canvas(width=300, height=300, bg='white')  
canvas.pack(expand=YES, fill=BOTH)                  
     
canvas.create_line(10, 10, 200, 200)
canvas.create_line(0, 300, 150, 150, width=10, fill='red')
canvas.create_oval(10, 10, 40, 40, width=2, fill='blue')
canvas.create_arc(200, 200, 300, 100)
canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')
photo=PhotoImage(file='1.gif')
canvas.create_image(250, 0, image=photo, anchor=NW)    
widget = Label(canvas, text='AAA', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)


mainloop()
