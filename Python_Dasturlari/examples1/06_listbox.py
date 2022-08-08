# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  06_listbox.py - список TListBox

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

def change(sender):
  print('selected now:', sender.selected)
  print('item[0]:', sender.item(0))
  print('items[0-2]:', sender.items(0, 2))

def keyPressed(event):
  print(event.keycode, ',', event.keysym, ',', event.char)

def changeMultiple(sender):
  fishLb.multiple = cbMulti.checked

app = TApplication("Использование списка TListBox")
app.position = (200, 200)
app.size = (310, 170)

fishLb = TListBox(app,
  values=["Лещ", 'Судак', "Налим", 'Карп', 'Барабулька'],
  selectmode='multiple', width = 120, height = 150 )
fishLb.background = "white"
fishLb.color = "black"
fishLb.font = ('Verdana', 10)
fishLb.position = (10, 10)
fishLb.selected = []
#fishLb.align="client"

cbMulti = TCheckBox( app, text = "множественный выбор" )
cbMulti.checked = fishLb.multiple
cbMulti.position = (140, 10)
cbMulti.onChange = changeMultiple

fishLb.onMouseMove = mouseMove
fishLb.onClick = click
fishLb.onDblClick = dblClick
fishLb.onEnter = enter
fishLb.onLeave = leave
fishLb.onKey = keyPressed
fishLb.onChange = change

app.run()

