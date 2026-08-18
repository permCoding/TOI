def int_to_bin(num: int) -> str:
    """
        перевести десятичное 0 <= num < 2**32
        в двоичное представление
    """
    # return bin(num)
    # return bin(num)[2:]
    # return f"{num:08b}"
    # return format(num, '08b')
    result = ''
    while num > 0:
        result += '01'[num % 2]
        num //= 2  # тут делением на основание
    return result[::-1]


def float_to_bin(num: float, precision = 12) -> str:
    """
        перевести десятичное 0 <= num < 1
        в двоичное представление
    """
    result = "0."
    for _ in range(precision):
        num *= 2
        if num >= 1:
            result += "1"
            num -= 1
        else:
            result += "0"
        if num == 0: break
    return result


# print(int_to_bin(19))
print(float_to_bin(0.5))    # 0.1
print(float_to_bin(0.25))   # 0.01
print(float_to_bin(0.125))  # 0.001

print(float_to_bin(0.1, 20))  # 0.001
print(float_to_bin(0.2, 20))  # 0.001
print(float_to_bin(0.3, 20))  # 0.001
print(float_to_bin(0.4, 20))  # 0.001

print(.1 + .2, "!=", .3, .1+.2 == .3)

# = = = = = = = = 

from decimal import Decimal

# десятичное значение хранимой двоичной дроби
print(Decimal.from_float(0.1))
# Вывод: 0.1000000000000000055511151231257827021181583404541015625
print(len(str(Decimal.from_float(0.1))))  # 57 знаков

# как число float представлено в виде дроби
pair = (0.1).as_integer_ratio()
print(pair)  # (3602879701896397, 36028797018963968)
print(pair[0] / pair[1])

# = = = = = = 
import sys

x, y, t, p = 12, 1.2, 2**24, 2**30
print(sys.getsizeof(x))  # 28
print(sys.getsizeof(y))  # 24
print(sys.getsizeof(t))  # 28
print(sys.getsizeof(p))  # 32