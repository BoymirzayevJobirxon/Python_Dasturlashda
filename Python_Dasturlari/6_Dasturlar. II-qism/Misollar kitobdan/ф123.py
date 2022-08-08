 class Class1:
    var1 = 10 
    def f_test(self): 
        return self.var1 
c1 = Class1()                    # Создаем экземпляр класса 
print (getattr(c1, "var1"))        # Выведет: 10 
print (getattr(c1, "f_test"))    # Выведет: 10 
print (getattr(c1, "var2", 0))     # Выведет: 0, т. к. атрибут не найден 
setattr(c1, "var2", 20)          # Создаем атрибут var2 
print (getattr(c1, "var2", 0))     # Выведет: 20 
delattr(c1, "var2")              # Удаляем атрибут var2 
print (getattr(c1, "var2", 0))     # Выведет: 0, т. к. атрибут не найден 
print (hasattr(c1, "var1"))        # Выведет: True 
print (hasattr(c1, "var2"))        # Выведет: False
