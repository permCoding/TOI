x = 42

print(type(x))        # <class 'int'>
print(dir(x))         # список методов
print(id(x))          # адрес объекта в памяти

# у объектов есть методы
print(x.bit_length()) # 6 - 101010
print(x.bit_count())  # 3 - 101010
print((10).bit_count())  # 2 - 1010

import sys
print(sys.getsizeof(x))  # 28

print(bin(x), oct(x), hex(x))
# 0b101010 0o52 0x2a

print(int('10'), int('10', 2), \
    int('10', 8), int('10', 16), \
    int('10', 36)
)  # 10 2 8 16 36

# - - - - - - - - 

a, b = 5, 3

print(a + b)       # 8
print(a.__add__(b))  # 8

print(a * b)       # 15
print(a.__mul__(b))  # 15

print(a ** b)      # 125
print(a.__pow__(b))  # 125

print(a // b)      # 1
print(a.__floordiv__(b))  # 1

# - - - - - - -

a, b, c = 42, 42, 43

# Сравнения
print(a.__eq__(b))   # True (a == b)
print(a.__ne__(c))   # True (a != c)
print(a.__lt__(c))   # True (a < c)
print(c.__gt__(a))   # True (c > a)

# - - - - - - - -

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# 9 => 1001
# 8 => 1000

print(is_power_of_two(9))  # False
print(is_power_of_two(8))  # True

# или есть метод объекта
print((9).bit_count() == 1)  # False
print((8).bit_count() == 1)  # True

print(bin(9).count('1') == 1)  # False
print(bin(8).count('1') == 1)  # True