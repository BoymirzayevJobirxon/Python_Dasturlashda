# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  09_groupbox.py - группа TGroupBox

"""
from simpletk import *

def mouseMove(event):
  print('(', event.x, ',', event.y, ')')

def click(event):
  print('* (', event.x, ',', event.y, ')')

def dblClick(event):
  print('** (', event.x, ',', event.y, ')')

def enter(event):
  print('enter')

def leave(event):
  print('leave')

def keyPressed(event):
  print(event.keycode, ',', event.keysym, ',', event.char)

def onChange(sender):
  s = "?"
  bkColor = "SystemButtonFace"
  try:
    r = int(rEdit.text)
    g = int(gEdit.text)
    b = int(bEdit.text)
    if r in range(256) and \
       g in range(256) and b in range(256):
      s = "#{:02X}{:02X}{:02X}".format(r, g, b)
      bkColor = s
  except:
     pass
  rgbLabel.text = s
  rgbRect.background = bkColor

bkColor = "#FEFEE2"

app = TApplication("Использование группы TGroupBox")
app.position = (200, 200)
app.size = (280, 150)
app.background = bkColor

f = ("Helvetica", 14)
gb = TGroupBox( app, text = "Это группа",
                width = 250, height = 125,
                padx = 10, pady = 10, relief = RIDGE )
gb.position = (10, 10)
#gb.align="client"
gb.background = bkColor
gb.color = "black"
gb.font = f

gb.onMouseMove = mouseMove
gb.onClick = click
gb.onDblClick = dblClick
gb.onEnter = enter
gb.onLeave = leave
gb.onKey = keyPressed

fSans = ("MS Sans Serif", 12)
lblR = TLabel(gb, text="R = ", font=fSans, bg = bkColor )
lblR.position = (5, 5)
lblG = TLabel(gb, text="G = ", font=fSans, bg = bkColor )
lblG.position = (5, 30)
lblB = TLabel(gb, text="B = ", font=fSans, bg = bkColor )
lblB.position = (5, 55)

fCourier = ("Courier New", 16, "bold")
rgbLabel = TLabel(gb, text="#000000", font=fCourier, fg="navy", bg = bkColor )
rgbLabel.position = (100, 5)

rgbRect = TLabel(gb, text="", width =90, height = 44 )
rgbRect.position = (105, 35)

rEdit = TEdit(gb, font=fSans, width=50)
rEdit.position = (45, 5)
rEdit.text = "123"

gEdit = TEdit(gb, font=fSans, width=50)
gEdit.position = (45, 30)
gEdit.text = "56"

bEdit = TEdit(gb, font=fSans, width=50)
bEdit.text = "80"
bEdit.position = (45, 55)

rEdit.onChange = onChange
gEdit.onChange = onChange
bEdit.onChange = onChange

app.run()

