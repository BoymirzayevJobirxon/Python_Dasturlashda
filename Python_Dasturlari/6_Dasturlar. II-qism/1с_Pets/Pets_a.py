"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1c. Домашние животные - наследование

  PETS_A.PY - начальный вариант

"""

#---------------------------------------------
#  Класс Pet - домашнее животное
#---------------------------------------------
class Pet:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    if not hasattr ( self, "say" ):
      raise NotImplementedError(
            "Нельзя создать такой объект!")
  def gettingOlder(self):
    self.__age += 1
  def getName(self):
    return self.__name
  name = property(getName)
  age = property(lambda x: x.__age)

#---------------------------------------------
#  Класс Cat - кошка
#---------------------------------------------
class Cat(Pet):
  def say(self):
    print( "{}: Мяу!".format(self.name) )

#---------------------------------------------
#  Класс Dog - собака
#---------------------------------------------
class Dog(Pet):
  def say(self):
    print( "{}: Гав!".format(self.name) )

#---------------------------------------------
#  Основная программа
#---------------------------------------------
p = Dog("Шарик", 5)
p.gettingOlder()
print( p.name + ":", p.age, "лет")
pets = [ p, Cat("Мурка", 3) ]
for p in pets:
  p.say()