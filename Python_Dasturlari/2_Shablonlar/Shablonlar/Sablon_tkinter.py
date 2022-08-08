from tkinter import *
from math import *
import tkinter as tk
import tkinter.ttk as ttk
from sys import argv

#root1 = tk.Tk()
root=Tk()

root.geometry('350x580+300+200') # ширина=500, высота=400, x=300, y=200
root.title("Sablon_tkinter")


button2 = Button(root,text='ok',width=6,height=1,
          bg='#ffefff',fg='#000000',font='arial 10')
button2.place(x=10,y=10)

w = Label(root, text="Hello, world!")
w.place(x=10,y=40)

text1=Text(root,height=4,width=15,font='Arial 8',wrap=WORD)
text1.insert(1.0,'Добавить Текст\n\ в начало первой строки')
text1.place(x=100,y=5)

entry = Entry(root, bd=5, width=20, show="DDD")
entry.place(x=10,y=70)

listbox1=Listbox(root,height=5,width=15,selectmode=EXTENDED)
list1=["Москва","Санкт-Петербург","Саратов","Омск"]
for i in list1:
    listbox1.insert(END,i)
listbox1.place(x=10,y=100)

frame1=Frame(root,bg='red',bd=7)
button1=Button(frame1,text=u'Первая кнопка')
frame1.place(x=10,y=190)
button1.pack()

var1=IntVar()
check1=Checkbutton(root,text='1 пункт',variable=var1,onvalue=1,offvalue=0)
check1.place(x=10,y=240)

var=IntVar()
rbutton1=Radiobutton(root,text='1',variable=var,value=1)
rbutton2=Radiobutton(root,text='2',variable=var,value=2)
rbutton1.place(x=10,y=270)
rbutton2.place(x=10,y=300)

def getV(root):
    a = scale1.get()
    print ("Значение", a) 
scale1 = Scale(root,orient=HORIZONTAL,length=200,from_=50,to=70,tickinterval=5,
               resolution=5)
button1 = Button(root,text=u"Получить значение")
scale1.place(x=10,y=330)
button1.place(x=10,y=390)
button1.bind("<Button-1>",getV)

text = Text(root, height=3, width=25)
text.place(x=10,y=420)
scrollbar = Scrollbar(root)
scrollbar.place(x=200,y=420)
# первая привязка
scrollbar['command'] = text.yview
# вторая привязка
text['yscrollcommand'] = scrollbar.set



frame = Frame(root)
frame.grid()
combobox = ttk.Combobox(frame,values = [u"ОДИН",u"ДВА",u"ТРИ"],height=3)
combobox.set(u"ОДИН")
combobox.grid(column=0,row=0)
frame.place(x=10,y=480)


pb = ttk.Progressbar(root, length=200)
pb.place(x=10,y=510)
pb.start(200)


def callback(e):
    print('Нажата кнопка', e.widget('text'))

button1 = Button(root, text='1')
button1.place(x=10,y=540)
button2 = Button(root, text='2')
button2.place(x=30,y=540)
root.bind_class('Button', '<1>', callback)


def leftclick(event):
    print('Вы нажали левую кнопку мыши')
def rightclick(event):
    print('Вы нажали правую кнопку мыши')
button1=Button(root, text=u'Нажми')
button1.place(x=100,y=540)
button1.bind('<Button-1>', leftclick)
button1.bind('<Button-3>', rightclick)


filename = 'a.gif'   
img = PhotoImage(file=filename)
can = Canvas(root)
can.place(x=130,y=100)
can.config(width=img.width(), height=img.height())  
can.create_image(2, 2, image=img, anchor=NW)

"""
#Canvas  grafika 
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
"""






root.mainloop()


