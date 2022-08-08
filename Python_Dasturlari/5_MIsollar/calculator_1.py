
from model import calc
from simpletk import *

app = TApplication("Калькулятор")
app.size = (200, 150)

inp = TComboBox(app, values=[])
inp.align = "top"
inp.text = "2+2"

answers = TListBox(app, values = [])
answers.align = "client"

def doCalc(event):
  ENTER = 13
  if event.keycode == ENTER:
    expr = inp.text
    x = calc(expr)
    answers.insert(0, expr+"="+str(x))
    if not inp.findItem(expr):
      inp.addItem(expr)

inp.onKey = doCalc

app.run()
