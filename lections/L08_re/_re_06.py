import re


text = "hello-hello world-world test-test"

comp = re.compile(r'\b(\w+)-\1\b', re.I)
matches = comp.findall(text)
print(matches)  # ['hello', 'world', 'test']

comp = re.compile(r'\b(?P<first>\w+)-(?P=first)\b', re.I)
matches = comp.findall(text)
print(matches)  # ['hello', 'world', 'test']

# - - - - - - - - - - - - -

text = "тик-так тик-ток тук-тук"

comp = re.compile(r'\b(\w+)-(\w+)\b', re.I)
# Меняем местами группы: \2 - \1
result = comp.sub(r'\2-\1', text)
print(result)  # так-тик ток-тик тук-тук

comp = re.compile(r'\b(\w+)-(\w+)\b', re.I)
# Меняем местами только первое совпадение
result = comp.sub(r'\2-\1', text, count=1)
print(result)  # так-тик тик-ток тук-тук

# - - - - - - - - - - 

# через именованные группы

text = "тик-так тик-ток тук-тук"

# Создаём именованные группы: first и second
pattern = re.compile(r'\b(?P<first>\w+)-(?P<second>\w+)\b', re.IGNORECASE)

# В строке замены ссылаемся на группы по именам
result = pattern.sub(r'\g<second>-\g<first>', text)
print(result)  # так-тик ток-тик тук-тук
