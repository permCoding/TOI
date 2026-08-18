import re

print(re.search(r'^Python', 'Python is lang...'))
print(re.search(r'Python!$', '... Python!'))
print(re.search(r'^Python$', 'Python'))

print(re.search(r'\bPython\b', '... Python ...'))
print(re.search(r'\bPython\b', '... Python! ...'))

print(re.search(r'\Bth\B', '... then ...'))
print(re.search(r'\Bth\B', '... Python ...'))

print(re.search(r'\bкот\B', ', который ...'))
print(re.search(r'\bкот\b', '... Кот ...', re.I))

text = "Кот, собака и 2 птицы."
words = re.findall(r'\w+', text)
print(words)  # ['Кот', 'собака', 'и', '2', 'птицы']


# найти слова только из латиницы
text = "Hello, мир - Python!"
latin_words = re.findall(r'\w+', text, re.ASCII)
print(latin_words)  # ['Hello', 'Python'] 


"""
\w - символ для слов
Режим ASCII (re.ASCII)
- если установить этот флаг, то 
  \w будет включать только латинские буквы [a-zA-Z], цифры [0-9] и символ подчеркивания _
  кириллица перестанет считаться "буквой", и границы слова будут проходить внутри русских слов. Например, для слова "кот" будут найдены границы между к и о, что почти всегда ломает логику поиска.
"""

"""
^	Начало строки
$	Конец строки
\b	Граница слова
\B	Не граница слова
"""