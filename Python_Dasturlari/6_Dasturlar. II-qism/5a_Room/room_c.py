# -*- coding: utf-8 -*-
"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 5a. Программы с графическим интерфейсом

  ROOM_C.py - поклейка обоями с сохранением

"""
from simpletk import *
from tkinter.messagebox import askokcancel
from tkinter import filedialog

#------------------------------------------
#  Главное окно
#------------------------------------------
app = TApplication("Обои")
app.size = (330, 170)
app.position = (200, 200)
app.resizable = (False, False)

def AskOnExit():
  if askokcancel("Подтверждение",
     "Вы действительно хотите выйти из программы?"):
    app.destroy()
app.onCloseQuery = AskOnExit

#------------------------------------------
#  Метки
#------------------------------------------
fSans = ("MS Sans Serif", 12)
lblL = TLabel(app, text="Длина =                     м", font=fSans )
lblL.position = (5, 5)

lblW = TLabel(app, text="Ширина =                  м", font=fSans )
lblW.position = (5, 30)

lblH = TLabel(app, text="Высота =                  м", font=fSans )
lblH.position = (5, 55)

lblR = TLabel(app, text="В рулоне                  кв. м", font=fSans )
lblR.position = (5, 80)

lblArea = TLabel(app, text="Площадь стен = 1 кв. м", font=fSans, fg="navy" )
lblArea.position = (5, 105)

lblN = TLabel(app, text="Нужно ? рулона (ов)", font=fSans, fg="navy" )
lblN.position = (5, 130)

#------------------------------------------
#  Поля ввода
#------------------------------------------
lEdit = TEdit( app, font = fSans, width = 50 )
lEdit.position = (90, 5)
lEdit.text = "5"

wEdit = TEdit( app, font = fSans, width = 50 )
wEdit.position = (90, 30)
wEdit.text = "3"

hEdit = TEdit( app, font = fSans, width = 50 )
hEdit.position = (90, 55)
hEdit.text = "3.5"

REdit = TEdit( app, font = fSans, width = 50 )
REdit.position = (90, 80)
REdit.text = "8"

#------------------------------------------
#  Обработчик изменений полей ввода
#------------------------------------------
def onChange(sender):
  s = sN = "?"
  try:
    l = float(lEdit.text)
    w = float(wEdit.text)
    h = float(hEdit.text)
    R = float(REdit.text)
    if l >= 0 and w >= 0 and h >= 0 and R > 0:
      S = h*2*(l+w)
      s = "{:0.2f}".format( S )
      N = int(S // R)
      if S % R > 0: N += 1
      sN = str(N)
  except:
     pass
  lblArea.text = "Площадь стен = " + s + " кв. м"
  lblN.text = "Нужно " + sN + " рулона (ов)"

lEdit.onChange = onChange
wEdit.onChange = onChange
hEdit.onChange = onChange
REdit.onChange = onChange

#------------------------------------------
#  Кнопки
#------------------------------------------
saveBtn = TButton ( app, width = 120, text = "Сохранить", font = fSans )
saveBtn.position = (200, 5)

loadBtn = TButton ( app, width = 120, text = "Загрузить", font = fSans )
loadBtn.position = (200, 45)

#------------------------------------------
#  Обработчик: загрузка данных из файла
#------------------------------------------
def loadFile ( sender ):
  fname = filedialog.askopenfilename(
     filetypes = [ ("Файлы DAT", "*.dat"), ("Все файлы", "*.*")] )
  if fname:
    with open(fname) as f:
      s = f.readline()
      print(s)
      try:
        l, w, h, R = map(float, s.split())
        print(l, w, h, R)
        lEdit.text = str(l)
        wEdit.text = str(w)
        hEdit.text = str(h)
        REdit.text = str(R)
      except:
        pass

#------------------------------------------
#  Обработчик: сохранение данных в файле
#------------------------------------------
def saveFile ( sender ):
  try:
    l = float(lEdit.text)
    w = float(wEdit.text)
    h = float(hEdit.text)
    R = float(REdit.text)
  except:
    return
  fname = filedialog.asksaveasfilename(
     filetypes = [ ("Файлы DAT", "*.dat"), ("Все файлы", "*.*")] )
  if fname:
    with open(fname,"w") as f:
      f.write( str(l) + " " + str(w) + " " + str(h) + " " + str(R) )

saveBtn.onClick = saveFile
loadBtn.onClick = loadFile

app.run()
