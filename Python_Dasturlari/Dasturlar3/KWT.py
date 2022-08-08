#Modullarni ulash
#______________________________________
import math
from simpletk import *
#______________________________________

#Ekranni tozalash prosedurasi
#--------------------------------------
def runCls(sender):
  aEdit.text = ''
  bEdit.text = ''
  cEdit.text = ''
#--------------------------------------

#Ifodalarni hisoblash prosedurasi  
#=======================================  
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
  
  s = "x1 = %.2f" % x1 
  s1 = "x2 = %.2f" % x2
  x1label.text = s
  x2label.text = s1
#========================================= 


#Asosiy dastur
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
app = TApplication("Kvadrat tenglama")
app.size = (240, 230)
app.position = (200, 200)
 
f = ("MS Sans Serif", 12)
lblR = TLabel(app, text="A = ", font=f )
lblR.position = (5, 5)
lblG = TLabel(app, text="B = ", font=f )
lblG.position = (5, 30)
lblB = TLabel(app, text="C = ", font=f )
lblB.position = (5, 55)

fc = ("Courier New", 16, "bold")
x1label = TLabel(app, text="x1 = ", font=fc, fg="navy" )
x1label.position = (10, 95)

x2label = TLabel(app, text="x2 = ", font=fc, fg="navy" )
x2label.position = (10, 120)

aEdit = TEdit(app, font=f, width=155)
aEdit.position = (45, 5)
aEdit.text = "0"

bEdit = TEdit(app, font=f, width=155)
bEdit.position = (45, 30)
bEdit.text = "0"

cEdit = TEdit(app, font=f, width=155)
cEdit.text = "0"
cEdit.position = (45, 55)

btnRun = TButton(app, text="   hisoblash   ")
btnRun.position = (80, 160)

btnCls = TButton(app, text="    tozalash    ")
btnCls.position = (80, 190)

btnRun.onClick = runEnter
btnCls.onClick = runCls

#app.screen.exitonclick()
#app.Run()
app.mainloop()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
