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

def tryToEnter(sender):
  if userEdit.text == "sysdba" and \
     passEdit.text == "masterkey":
     print("OK.")
     app.destroy()

app = TApplication("Вход в систему")
app.position = (200, 200)
app.size = (200, 120)

userEdit = TEditPanel( app, "Пользователь" )
userEdit.align = "top"

passEdit = TEditPanel( app, "Пароль" )
passEdit.align = "top"
btn = TButton(app, text="   Войти   ")
btn.position = (70, 85)
btn.onClick = tryToEnter

app.default = btn

app.run()
