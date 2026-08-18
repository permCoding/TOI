# генераторное выражение
gen_1 = (x**2 for x in (1,2,3))

# эквивалент - функция-генератор:
def _gen():
    for x in 1,2,3:
        yield x**2

gen_2 = _gen()

print(gen_1)
# <generator object <genexpr> at 0x0000019CFE521220>
print(gen_2)
# <generator object _gen at 0x0000019CFE521700>
print(list(gen_1))  # [1, 4, 9]
print(list(gen_2))  # [1, 4, 9]