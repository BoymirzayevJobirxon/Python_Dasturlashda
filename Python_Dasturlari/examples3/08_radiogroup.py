# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  08_radiogroup.py - группа радиокнопок TRadioGroup

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

app = TApplication("Использование радиогрупп TRadioGroup")
app.position = (200, 200)
app.size = (500, 210)

rg = TRadioGroup(app,
          values = ["Python", 'C++', "Java", 'Haskell', 'Kotlin'],
          width = 150, height = 180, padx = 10, pady = 10)
rg.position = (10, 10)
rg.background = "#FEFEE2"
rg.color = "black"
rg.font = ('Consolas', 12)
rg.selected = 2
#rg.align="client"

def change(sender):
  print('Selected now:', sender.selected,
                         sender.item(sender.selected))

rg.onMouseMove = mouseMove
rg.onClick = click
rg.onDblClick = dblClick
rg.onEnter = enter
rg.onLeave = leave
rg.onKey = keyPressed
rg.onChange = change

rg2 = TRadioGroup(app,
          values = ["MongoDB", 'Redis', "Cassandra"],
          orient = HORIZONTAL,
          width = 300, height = 50, padx = 10, pady = 10)
rg2.position = (180, 10)
rg2.background = "#EEEEEE"
rg2.color = "black"
rg2.font = ('Helvetica', 11)
rg2.selected = 1
rg2.onChange = change
#rg.align="client"

app.run()

