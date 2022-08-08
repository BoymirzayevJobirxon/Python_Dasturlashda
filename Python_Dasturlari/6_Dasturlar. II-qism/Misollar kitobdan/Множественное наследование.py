class Class1:         # Базовый класс для класса Class2 
    def f_func1(self): 
        print ("Метод f_func1() класса Class1") 
class Class2(Class1): # Класс Class2 наследует класс Class1 
    def f_func2(self): 
        print ("Метод f_func2() класса Class2") 
class Class3(Class1): # Класс Class3 наследует класс Class1 
    def f_func1(self): 
        print ("Метод f_func1() класса Class3") 
    def f_func2(self): 
        print ("Метод f_func2() класса Class3") 
    def f_func3(self): 
        print ("Метод f_func3() класса Class3") 
    def f_func4(self): 
        print ("Метод f_func4() класса Class3") 
class Class4(Class2, Class3): # Множественное наследование 
    def f_func4(self): 
        print ("Метод f_func4() класса Class4") 
c1 = Class4()             # Создаем экземпляр класса Class4 
c1.f_func1()              # Выведет: Метод f_func1() класса Class1 
c1.f_func2()              # Выведет: Метод f_func2() класса Class2 
c1.f_func3()              # Выведет: Метод f_func3() класса Class3 
c1.f_func4()              # Выведет: Метод f_func4() класса Class4 
