import re

# Функция: флаги можно менять при каждом вызове
re.search(r'abc', 'ABC')
re.search(r'abc', 'ABC', re.IGNORECASE)

# Компиляция: флаги фиксируются
pattern = re.compile(r'abc', re.IGNORECASE)
pattern.search('ABC')   # флаг уже внутри


# Упрощённо
def search(pattern, text, flags=0):
    compiled = re.compile(pattern, flags)  # ← компиляция
    return compiled.search(text)           # ← поиск


import re

# Функции модуля re
re.search(r'abc', 'ABC', re.IGNORECASE | re.MULTILINE)
re.search(r'abc', 'ABC', re.I | re.M)

# При компиляции
pattern = re.compile(r'abc', re.IGNORECASE | re.MULTILINE)
pattern.search('ABC')