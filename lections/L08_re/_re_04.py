# Важно: По умолчанию . не совпадает с символом новой строки (\n).
import re

lst = ['ct', 'cat', 'cot', 'caaaat', 'cart', 'c.t']

for s in lst: print(re.search(r'c.t', s))
print()
for s in lst: print(re.search(r'c..t', s))
print()
for s in lst: print(re.search(r'ca*t', s))
print()
for s in lst: print(re.search(r'c.*t', s))
print()
for s in lst: print(re.search(r'ca+t', s))
print()
for s in lst: print(re.search(r'ca?t', s))
print()
for s in lst: print(re.search(r'c\.t', s))
print()
for s in lst: print(re.search('c\\.t', s))