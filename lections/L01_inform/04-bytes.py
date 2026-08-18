s = "строка"

b = bytes(s, "utf-8")

print(type(b))  # <class 'bytes'>
# длина в символах и в байтах
print(len(s), len(b))  # 6 12
print(b)
# b'\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0'

b = bytes(s, "cp1251")

print(type(b))  # <class 'bytes'>
print(len(s), len(b))  # 6 6 
print(b)  # b'\xf1\xf2\xf0\xee\xea\xe0'
# b[1] = 238  # неизменяемый тип
print(b.decode('cp1251'))  # строка

# - - - - - - - - - - - - - -

b = b"0123 string" # только для символов из ASCII
print('b -', type(b))  # <class 'bytes'>
print(len(b))  # 6
print(b, b.decode())
# b'\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0'

# - - - - - - - - - - - - - - 

for ind, elm in enumerate(b): 
   print(ind, elm)
# 0 241
# 1 242
# 2 240
# 3 238
# 4 234
# 5 224

# - - - - - - - - - - - - - -

b = bytearray("строка", "cp1251")
print(type(b))  # <class 'bytearray'>
print(len(s), len(b))  # 6 6 
print(b)  # b'\xf1\xf2\xf0\xee\xea\xe0'
b[1] = 238  # изменяемый тип
print(b.decode('cp1251'))  # сорока

def func(): return ...
print(type(func))  # <class 'function'>

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y
print(type(Point))  # <class 'type'>

import sys
print(type(sys))  # <class 'module'>