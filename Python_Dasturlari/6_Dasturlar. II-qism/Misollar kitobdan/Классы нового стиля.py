class Class1:          # Классический класс 
    pass 
class Class2(object):  # Класс нового стиля 
    pass 
class Class3(list):    # Класс нового стиля 
    pass 
print (type(Class1))     # Выведет: <type 'classobj'> 
print (type(Class2))     # Выведет: <type 'type'> 
print (type(Class3))     # Выведет: <type 'type'> 
                       # __bases__ содержит кортеж с базовыми классами 
print (Class1.__bases__) # Выведет: () 
print (Class2.__bases__) # Выведет: (<type 'object'>,) 
print (Class3.__bases__)# Выведет: (<type 'list'>,) 
c1, c2, c3 = Class1(), Class2(), Class3() 
print (c1.__class__ )    # Выведет: __main__.Class1 
print (c2.__class__ )    # Выведет: <class '__main__.Class2'> 
print (c3.__class__ )    # Выведет: <class '__main__.Class3'> 
print (type(c1))         # Выведет: <type 'instance'> 
print (type(c2))         # Выведет: <class '__main__.Class2'> 
print (type(c3))        # Выведет: <class '__main__.Class3'> 
