from simpletk import *
from tkinter.messagebox import askokcancel
def askOnExit():
  if askokcancel ( "Bajarilsinmi", "Dasturdan chiqasizmi?" ):
    app.destroy()
def mouseMove(event):
  print('(', event.x, ',', event.y, ')')
def click(event):
  print('* (', event.x, ',', event.y, ')')
def dblClick(event):
  print('** (', event.x, ',', event.y, ')')
def keyPressed(event):
  print('key', event.keycode, ',', event.keysym, ',', event.char)
def resize(event):
  print('resize (', event.x, ',', event.y, ',', event.width, ',',
       event.height, ')')
def enter(event):
  print('enter')
def leave(event):
  print('chegaradan chiqdi')
app = TApplication("Birinchi forma")
app.position = (100, 300)
app.size = (500, 200)
app.minsize = (100, 200)
app.maxsize = (900, 700)
app.resizable = (True, False)
app.background = "white"
app.onCloseQuery = askOnExit
app.onMouseMove = mouseMove
app.onClick = click
app.onDblClick = dblClick
app.onResize = resize
app.onKey = keyPressed
app.onEnter = enter
app.onLeave = leave
print(app.title)
app.title = "Bu amaliyot uchun birinchi forma!"
print(app.title)
app.run()

