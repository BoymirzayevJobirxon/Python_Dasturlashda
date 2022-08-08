
from simpletk import *

app = TApplication("RGB-кодирование")
app.size = (210, 90)
app.position = (200, 200)
 
f = ("MS Sans Serif", 12)
lblR = TLabel(app, text="R = ", font=f )
lblR.position = (5, 5)
lblG = TLabel(app, text="G = ", font=f )
lblG.position = (5, 30)
lblB = TLabel(app, text="B = ", font=f )
lblB.position = (5, 55)

fc = ("Courier New", 16, "bold")
rgbLabel = TLabel(app, text="#000000", font=fc, fg="navy" )
rgbLabel.position = (100, 5)

rgbRect = TLabel(app, text="", width =15, height = 3 )
rgbRect.position = (105, 35)

rEdit = TEdit(app, font=f, width=5)
rEdit.position = (45, 5)
rEdit.text = "123"

gEdit = TEdit(app, font=f, width=5)
gEdit.position = (45, 30)
gEdit.text = "56"

bEdit = TEdit(app, font=f, width=5)
bEdit.text = "80"
bEdit.position = (45, 55)

def onChange(sender):
  hexColor = "?"
  bkColor = 'SystemButtonFace'
  try:
    r = int(rEdit.text)
    g = int(gEdit.text)
    b = int(bEdit.text)
    if r in range(256) and \
       g in range(256) and b in range(256):
      hexColor = "#{:02x}{:02x}{:02x}".format(r, g, b)
      bkColor = hexColor
  except:
    pass
    rgbLabel.text = hexColor
    rgbRect.background = bkColor

rEdit.onChange = onChange
gEdit.onChange = onChange
bEdit.onChange = onChange

app.Run()
