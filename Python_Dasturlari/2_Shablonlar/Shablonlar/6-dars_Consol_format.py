# -*- coding: utf-8 -*-

from simpletk import *

a = 123
print( ">{:d}<".format(a) )
print( ">{:o}<".format(a) )
print( ">{:x}<".format(a) )
# print( ">{:s}<".format(a) )

x = 1.2345678
print( x )
print( ">{:7.3f}<".format(x) )

app = TApplication("Первая форма")
app.Run()
