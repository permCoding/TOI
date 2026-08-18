dct = {symbol:ord(symbol)-55 for symbol in 'ABCDEF'}
print(dct)  # hex
# {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
dct['0'] = 0  # добавить или заменить
key = 'F'
print(key in dct)    # True
# .pop() - возвращает val и удаляет key
print(dct.pop('F'))  # 15
print(key in dct)    # False
for key, val in dct.items():
    print(key, val)

st = set()
st.add(2); st.add(2); st.add(1)
print(len(st), st)  # 2 {1, 2}
st.discard(2)
print(len(st), st)  # 1 {1}

"""
в основе словаря (dict) в Python лежит хеш-таблица
которая обеспечивает прямой доступ к элементам по ключу, 
но это дополнительный расход памяти и 
нестабильный порядок элементов при расширении словаря

для каждого ключа формируется хеш
"""

print(hash('ABC'))     # 1433972551973331715
print(hash('Python'))  # 2068729341365198690

