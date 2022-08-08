# -*- coding: utf-8
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  10_intedit.py - cоздание нового компонента TIntEdit

"""

from simpletk import *
from int_edit import TIntEdit

f = ("Courier New", 14, "bold")

app = TApplication("Шестнадцатеричная система")
app.size = (250, 36)
app.position = (200, 200)

hexLabel = TLabel(app, text="?", font=f, fg="navy" )
hexLabel.position = (155, 5)

def onNumChange(sender):
  hexLabel.text = "{:X}".format(sender.value)

decEdit = TIntEdit(app, width=120, font = f)
decEdit.position = (5, 5)
decEdit.text = "1001"
decEdit.onChange = onNumChange

app.run()
