# -*- coding: utf-8 -*-

from simpletk import *

print( "Введите целое число:" )
d = int( input() )
a = d // 10   # = 8 
b = d % 10    # = 5 
print( a, " ",  b )
print( -7 // 2, -7 % 2 )
print( int(-1.6) )
print( round(-1.6) )
print( int(1.6) )
print( round(1.6) )
y = 2*a**2 + b**3
print ( y )

app = TApplication("Первая форма")
app.Run()
