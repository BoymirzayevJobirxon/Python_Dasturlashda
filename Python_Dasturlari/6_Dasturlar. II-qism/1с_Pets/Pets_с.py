"""
  Программы к учебнику информатики для 11 класса углублённого уровня.
  Авторы: К.Ю. Поляков, Е.А. Еремин
  E-mail: kpolyakov@mail.ru
  Сайт поддержки: http://kpolyakov.spb.ru

  Глава 7. Объектно-ориентированное программирование
  Проект № 1c. Домашние животные - наследование

  PETS_С.PY - добавление класса Reptilia и его
              наследников Turtle и Snake

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
#  Класс Mammal - млекопитающее
#---------------------------------------------
class Mammal(Pet):
  def run(self):
    print( "{} побежал...".format(self.name) )

#---------------------------------------------
#  Класс Cat - кошка
#---------------------------------------------
class Cat(Mammal):
  def say(self):
    print( "{}: Мяу!".format(self.name) )

#---------------------------------------------
#  Класс Dog - собака
#---------------------------------------------
class Dog(Mammal):
  def say(self):
    print( "{}: Гав!".format(self.name) )

#---------------------------------------------
#  Класс Replilia - пресмыкающееся
#---------------------------------------------
class Reptilia(Pet):
  def crawl(self):
    print( "{} пополз...".format(self.name) )

#---------------------------------------------
#  Класс Turtle - пресмыкающееся
#---------------------------------------------
class Turtle(Reptilia):
  def say(self):
    print( "{}: ...".format(self.name) )

#---------------------------------------------
#  Класс Snake - змея
#---------------------------------------------
class Snake(Reptilia):
  def say(self):
    print( "{}: ш-ш-ш-ш...".format(self.name) )

#---------------------------------------------
#  Основная программа
#---------------------------------------------
pets = [ Cat("Мурзик", 3), Turtle("Зак", 32),
         Dog("Шарик", 5), Snake("Чаки", 2) ]
for p in pets:
  p.say()
  if isinstance(p, Mammal):
    p.run()
  if isinstance(p, Reptilia):
    p.crawl()
