class Class1(object):  # Класс нового стиля 
#class Class1:         # Классический класс 
    var1 = "Это значение в классических классах" 
class Class2(Class1): pass 
class Class3(Class2): pass 
class Class4(Class3): pass 
class Class5(Class2): 
    var1 = "Это значение в классах нового стиля" 
class Class6(Class5): pass 
class Class7(Class4, Class6): pass 
c1 = Class7() 
print (c1.var1)
