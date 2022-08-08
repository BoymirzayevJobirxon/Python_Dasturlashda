from tkinter import *
from simpletk import *
from tkinter import filedialog

app = TApplication("Shablon_Simpletk")
app.size = (200, 620)
app.position = (200, 200)

memo = TMemo(app, height = 100, width = 195, bg = "white", fg = 'navy', wrap = "word")
memo.position = 5, 500

def changeCMY ( event = None ):
   changeRGB ( event )
Cyan = TTrackBar( app, [0, 255], width = 10, length = 175,
                  orient = HORIZONTAL, onTrack = changeCMY )
Cyan.value = 255
Cyan.position = (5, 450)

image = TImage(app)
image.picture = "flower.gif"
image.position = (5, 10)

f = ("MS Sans Serif", 12)
fc = ("Courier New", 16, "bold")
rgbLabel = TLabel(app, text="#000000", font=fc, fg="navy" )
rgbLabel.position = (5, 120)

rEdit = TEdit(app, font=f, width=190)
rEdit.position = (5, 190)
rEdit.text = "123"

btnRun = TButton(app, text="hisoblash")
btnRun.position = (5, 255)

flCb = TCheckBox(app, text = "ulagich")
flCb.position = (5, 225)

lbLB = TListBox(app,  values=["Samarqand"] )
lbLB.position = (5, 150)
lbLB.size = (205, 25)

vsCB = TComboBox(app, values=["Andijon"])
vsCB.position = (5, 295)
vsCB.size = (190, 25)

rg2 = TRadioGroup(app,
          values = ["RG1", 'RG2', "RG3"],
          orient = HORIZONTAL,
          width = 250, height = 50, padx = 10, pady = 10)
rg2.position = (1, 320)
rg2.background = "#EEEEEE"
rg2.color = "black"
rg2.font = ('Helvetica', 11)
rg2.selected = 1

f = ("Helvetica", 14)
gb = TGroupBox(app, text = "Bu gruppa",
                width = 180, height = 80,
                padx = 10, pady = 10, relief = RIDGE )
gb.position = (5, 370)
gb.background = '#B4A7B5'
gb.color = "black"
gb.font = f







app.mainloop()
#app.screen.exitonclick()
#app.Run()
