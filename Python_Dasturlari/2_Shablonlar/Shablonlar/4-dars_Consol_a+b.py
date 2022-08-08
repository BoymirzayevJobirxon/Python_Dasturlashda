# -*- coding: utf-8 -*-

from simpletk import *

print("   ") 
print ( "Введите два целых числа:" )
a, b = map( int,  input().split() )
c = a + b
print ( a, "+", b, "=", c, sep = "" )
 

app = TApplication("Первая форма")
app.Run()



