class Class4(Class2, Class3): # Множественное наследование 
                 # Наследуем f_func2() из класса Class3, а не из класса Class2 
    f_func2 = Class3.f_func2 
    def f_func4(self): 
        print ("Метод f_func4() класса Class4") 
