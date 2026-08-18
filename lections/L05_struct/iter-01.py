lst = list('025')
# ['0', '2', '5']

# for неявно вызывает iter() 
# затем next() до StopIteration
for item in lst: print(item)

# - - - - - - - - - - - - -

# создаём итератор
it = iter(lst)  # вызов метода объекта lst.__iter__()

# явно вызываем next()
print(next(it))  # 0
print(next(it))  # 2
print(next(it))  # 5
# eсли вызвать next() ещё раз:
# print(next(it))  # получим StopIteration

# - - - - - - - - - - - - -

it = iter(lst)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break

# - - - - - - - - - - - - -

it = iter(lst)
while (item := next(it, None)) is not None:
    print(item)

# - - - - - - - - - - - - -

# интерфейс итератора реализован в разных коллекциях
lst = [1, 2, 3]
tpl = (1, 2, 3)
line = "123"
st = {1, 2, 3}           # множество (порядок не гарантирован)
dct = {'a': 1, 'b': 2}   # словарь (итерация по ключам)

it = iter(dct)
print(dct[it.__next__()])  # 1
print(dct[it.__next__()])  # 2
for key in dct: print(key, dct[key])
# a 1
# b 2

import os
# __file__ — это встроенный атрибут, который 
# содержит путь к текущему файлу скрипта
file_name = os.path.basename(__file__)
print(f"Имя файла: {file_name}")
with open(file_name, 'r', encoding='utf8') as f:
    for line in f:   # итерация по строкам файла
        print(line, end='')

# - - - - - - - - - - - - -

# свой класс-итератор - сделаем так
# чтобы правая граница входила
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

my_range = MyRange(1, 4)
print(my_range)
print([elm for elm in my_range])
