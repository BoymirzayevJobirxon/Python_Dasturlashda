import math 
from simpletk import *

class TEditPanel(TPanel):
    def __init__(self, parent, label, **kw):
        TPanel.__init__(self, parent, **kw)
        self.autoSize = True
        self.label = TLabel(self, text=label )
        self.label.align = "top"
        self.edit = TEdit(self)
        self.edit.align = "top"
        

    def __getText(self):
      return self.edit.text

    def __setText(self, newText):
      self.edit.text = newText
    text = property(__getText, __setText)

def runEnter(sender):
  a = float(aEdit.text)
  b = float(bEdit.text)
  c = float(cEdit.text)

  d = math.pow((b*b-4*a*c),1/2)
  #d = b*b-4*a*c
  print('a = ',"%.2f" % a)
  print('b = ',"%.2f" % b)
  print('c = ',"%.2f" % c)
  print('d = ',"%.2f" % d)
  
  if d < 0 :
    print('echimga ega emes')
    x1label.text = 'echimga ega emes'
    x2label.text = ''
  elif d == 0:
     x1 = -b/(2*a)
     print('x1 = ',"%.2f" % x1) 
  else:     
     x1 = (-b+d)/(2*a)
     print('x1 = ',"%.2f" % x1)
     x2 = (-b-d)/(2*a)
     print('x2 = ',"%.2f" % x2)
  
  s = "%.2f" % x1 
  s1 = "%.2f" % x2
  x1label.text = s
  x2label.text = s1
 

def runCls(sender):
  aEdit.text = ''
  bEdit.text = ''
  cEdit.text = ''
  

app = TApplication("Kvadrat tenglama")
app.position = (200, 200)
app.size = (240, 280)

aEdit = TEditPanel( app, "a = ?", width=5  )
aEdit.align = "top"

bEdit = TEditPanel( app, "b = ?" )
bEdit.align = "top"

cEdit = TEditPanel( app, "c = ?" )
cEdit.align = "top"

x11label = TLabel(app, text="x1 = ")
x11label.position = (5, 130)
x1label = TLabel(app, text="#000000")
x1label.position = (30, 130)

x12label = TLabel(app, text="x2 = ")
x12label.position = (5, 160)
x2label = TLabel(app, text="#000000" )
x2label.position = (30, 160)
 
btnRun = TButton(app, text="   hisoblash   ")
btnRun.position = (80, 200)

btnCls = TButton(app, text="    tozalash    ")
btnCls.position = (80, 235)

btnRun.onClick = runEnter
btnCls.onClick = runCls

app.default = btnRun
app.default = btnCls

app.run()
