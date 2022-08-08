# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  07_combobox.py - выпадающий список TComboBox

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

app = TApplication("Использование выпадающего списка TComboBox")
app.position = (200, 200)
app.size = (350, 70)

cb = TComboBox(app,
               values=["Москва", 'Киров', "Грозный", 'Владивосток', 'Магадан'],
               width = 220
               )
cb.position = (10, 10)
cb.font = ('Georgia', 14)
#cb.align="client"

def validate(sender):
  print('validate', sender.text)
  return not '.' in sender.text

def change(sender):
  print('text now:', sender.text)

cb.onMouseMove = mouseMove
cb.onClick = click
cb.onDblClick = dblClick
cb.onEnter = enter
cb.onLeave = leave
cb.onKey = keyPressed
cb.onChange = change
cb.onValidate = validate

app.run()

