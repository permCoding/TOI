x = 10      # int
x = "hello" # str
x = 3.14    # float
y = x == x

print(y, type(y))  
# True <class 'bool'>

# = = = = = = = = = = float = = = = = = = = = = 

# используют для научных или инженерных расчётов

x, y = 1, 2
res = 1/2
print(type(res), res)  
# <class 'float'> 0.5

from math import pi
# pi = 3.1415926535...

radius = 5.0
area = pi * (radius ** 2)
print(area)  # 78.53981633974483
print(type(area), f"{area:0.5f}")
# <class 'float'> 78.53982

# можно задавать проценты или вероятности
probability = 0.85
total_score = 89.5

# проблема точности
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 != 0.3
print(result == 0.3)   # False

# сравнение с погрешностью (эпсилон)
eps = 1e-9  # зададим требуемую точность
if abs((0.1 + 0.2) - 0.3) < eps:
    print("Числа равны с учётом погрешности")

# преобразование из строки, файла, ввода пользователем
price_str = "1999.99"
price = float(price_str) * 1.2  # НДС 20%