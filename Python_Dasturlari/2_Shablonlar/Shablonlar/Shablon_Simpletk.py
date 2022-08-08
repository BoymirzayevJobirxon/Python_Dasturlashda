
from simpletk import *
from tkinter import filedialog

app = TApplication("Shablon_Simpletk")
app.size = (440, 680)
app.position = (200, 200)

image = TImage(app, bg="#eeeeee")
image.align = "client"
image.picture = "flower.gif"

f = ("MS Sans Serif", 12)
lblR = TLabel(app, text="A = ", font=f )
lblR.position = (160, 5)

fc = ("Courier New", 16, "bold")
rgbLabel = TLabel(app, text="#000000", font=fc, fg="navy" )
rgbLabel.position = (160, 50)

rEdit = TEdit(app, font=f, width=155)
rEdit.position = (160, 100)
rEdit.text = "123"

btnRun = TButton(app, text="hisoblash")
btnRun.position = (160, 150)

flCb = TCheckBox(app, text = "ulagich")
flCb.position = (5, 225)

lbLB = TListBox(app, values=["Samarqand"] )
lbLB.position = (5, 150)
lbLB.size = (120, 25)

vsCB = TComboBox(app, values=["Andijon"])
vsCB.position = (5, 295)
vsCB.size = (120, 25)

rg2 = TRadioGroup(app,
          values = ["RG1", 'RG2', "RG3"],
          orient = HORIZONTAL,
          width = 300, height = 50, padx = 10, pady = 10)
rg2.position = (1, 320)
rg2.background = "#EEEEEE"
rg2.color = "black"
rg2.font = ('Helvetica', 11)
rg2.selected = 1

f = ("Helvetica", 14)
gb = TGroupBox(app, text = "Bu gruppa",
                width = 180, height = 80,
                padx = 10, pady = 10, relief = RIDGE )
gb.position = (5, 390)
gb.background = bkColor
gb.color = "black"
gb.font = f




 
app.screen.exitonclick()
app.Run()
