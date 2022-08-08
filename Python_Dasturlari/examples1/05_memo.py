# -*- coding: utf-8 -*-
"""
  Демонстрационная программа к модулю SIMPLETK.
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  05_memo.py - использование текстового редактора TMemo

"""
from simpletk import *

def insertText(event):
  memo.insert(INSERT, lineEdit.text)

def deleteText(event):
  try:
    memo.delete(SEL_FIRST, SEL_LAST)
  except: pass

def copyText(event):
  text = memo.get(1.0, END)  # 1.0 - строка 1 (первая), столбец 0 (первый)
  saveMemo.text = text
  print(saveMemo.getLine(1))

def insertLine(event):
  saveMemo.insertLine(1, lineEdit2.text)

def deleteLine(event):
  saveMemo.deleteLine(1)

app = TApplication("Использование TMemo")
app.size = (500, 400)

topBar = TPanel(app, relief="raised", height=35, bd=1)
topBar.align = "top"

bottom = TPanel(app, height = 200 )
bottom.align = "bottom"

memo = TMemo(app, height = 100, bg = "white",           # фон
                  fg = 'navy',            # цвет символов
                  wrap = "word"           # перенос по словам
                  )
memo.position = 20, 20
memo.align = "client"
memo.font = ('Times New Roman', 12)

fSans = ("MS Sans Serif", 12)
lineEdit = TEdit(topBar, font=fSans, width=50)
lineEdit.position = (5, 5)
lineEdit.text = "Петя"

insBtn = TButton(topBar, width = 35, height = 25, text = "Ins" )
insBtn.position = (60, 5)
insBtn.onClick = insertText

delBtn = TButton( topBar, width = 35, height = 25, text = "Del" )
delBtn.position = (100, 5)
delBtn.onClick = deleteText

copyBtn = TButton( topBar, width = 35, height = 25, text = "Copy" )
copyBtn.position = (140, 5)
copyBtn.onClick = copyText

savePanel = TPanel( bottom, relief = "raised", height = 35, bd = 1 )
savePanel.align = "top"

saveMemo = TMemo( bottom, height = 100,
                  bg = "white",           # фон
                  fg = 'navy',            # цвет символов
                  wrap = "word"           # перенос по словам
                  )
saveMemo.align = "client"

lineEdit2 = TEdit( savePanel, font = fSans, width = 120 )
lineEdit2.position = (5, 5)
lineEdit2.text = "Вася"

insBtn2 = TButton( savePanel, width = 50, text = "Ins line 1" )
insBtn2.position = (140, 5)
insBtn2.onClick = insertLine

delBtn2 = TButton( savePanel, width = 50, text = "Del line 1" )
delBtn2.position = (200, 5)
delBtn2.onClick = deleteLine

app.run()
