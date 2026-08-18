# bool — подкласс int, наследует всё от целых чисел
# True == 1, False == 0
# в памяти всегда только один объект True и один False
# Занимает 28 байт как маленькое целое число
# Используется в условных выражениях, циклах, сравнениях

import sys

print(sys.getsizeof(1024))   # 28 байт
print(sys.getsizeof(True))   # 28 байт
print(sys.getsizeof(False))  # 28 байт
print(sys.getsizeof(1))      # 28 байт - как int


value = True
print(type(value))                # <class 'bool'>
print(isinstance(value, bool))    # True - объект класса ?
print(isinstance(value, int))     # True - потому что bool — это int
print(issubclass(bool, int))      # True
# логическое значение хранится как 0 или 1

# = = = = = = = = = = = = = = = 

print('- 1 -')
print(1 == True)  # True
print(0 == True)  # False
print(0 == False) # True
print(9 == True)  # False

print(1 is True)   # False - это разные объекты
print(0 is False)  # False - это разные объекты

a, b = True, True
print(a is b)  # True - один и тот же объект
print(id(True))  # - ссылка на объект
print(id(a))     # - ссылка на объект
print(id(b))     # - ссылка на объект

# = = = = = = = = = = = = = = = 

print('- 2 -')
x = (1 == 1)   # True - ссылка на объект
y = (2 == 2)   # True - ссылка на объект
# is - проверяет ссылки
# == - проверяет значения
print(x == y)
print(x is y)  # True (один и тот же объект True)
print(x == 1)
print(x is True)
print(1 is True)   # False - это разные объекты
print(id(True))  # - ссылка на объект
print(id(x))     # - ссылка на объект
print(id(y))     # - ссылка на объект

# = = = = = = = = = = = = = = = 

print('- 3 -')
b = 1  # далее три раза True
if b: print(b == 1)
if bool(b): print(b == 1)
if b.__bool__(): print(b == True)
# во встроенных объектах (классах)
# определён метод __bool__()

s = '';  print(bool(s))  # False
s = '1'; print(bool(s))  # True

dct = {}; print(bool(dct))  # False
lst = []; print(bool(lst))  # False

dct = {"id":101}; print(bool(dct))   # True
lst = [101]; print(bool(lst))        # True

"""
любой объект пользовательского типа
- по умолчанию истинный
- это может быть изменено при наличии
  в классе .__bool__()
"""
from math import hypot

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return hypot(self.x, self.y)

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

    def __bool__(self):  # переопределим bool
        return True if self.x != self.y else False

p1 = Point(3, 4)
print(p1, bool(p1))  # x = 3, y = 4 True
p2 = Point(0, 4)
print(p2, bool(p2))  # x = 0, y = 4 True
p3 = Point(0, 0)
print(p3, bool(p3))  # x = 0, y = 0 False
p4 = Point(4, 4)
print(p4, bool(p4))  # x = 0, y = 0 False