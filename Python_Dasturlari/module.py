from simpletk import *

app = TApplication("asdas")

e = TEdit(app, exportselection = True, borderwidth = 0 )
e.place( x = 10, y = 20, width = 50, height = 30 )
e.insert( 0, 'wqwqweqw' )
e.focus_force()

m = TMemo(app, width = 200, height = 120)
m.position = (50, 50)

app.run()