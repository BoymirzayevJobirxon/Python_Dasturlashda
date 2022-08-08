class Class1:               # Базовый класс 
    def __init__(self): 
        print ("Конструктор базового класса") 
    def f_func1(self): 
        print ("Метод f_func1() класса Class1") 
 
class Class2(Class1):       # Класс Class2 наследует класс Class1 
    def __init__(self): 
        print ("Конструктор производного класса") 
        Class1.__init__(self) # Вызываем конструктор базового класса 
    def f_func1(self): 
        print ("Метод f_func1() класса Class2") 
        Class1.f_func1(self)  # Вызываем метод базового класса 
 
c1 = Class2()                 # Создаем экземпляр класса Class2 
c1.f_func1()                  # Вызываем метод f_func1()
