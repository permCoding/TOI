a = [
    ('Allo', 2),
    ('Ball', 1),
    ('Car', 2), 
    ('Astro', 3), 
    ('Winny', 2), 
    ('Char', 1),
    ('Wim', 3)
]  

# сортировать по двум параметрам:
#     1. по первому параметру - по номеру по убыванию
#     2. по второму параметру - по названию по возрастанию

# в Python используется стабильная сортировка
srtd_0 = sorted(a, key = lambda x : x[0])
t = sorted(srtd_0, key = lambda x : x[1], reverse = True)
# и так далее можно сортировать по любому количеству параметров

# ORDER BY name DESC, ball ASC, id ASC - это сортировка в SQL


t = sorted(
    sorted(a, key = lambda x : x[0]), 
    key = lambda x : x[1], 
    reverse = True
)  

for row in t: print(row[1], row[0])

"""
3 Astro
3 Wim
2 Allo
2 Car
2 Winny
1 Ball
1 Char

('Astro', 3)
('Wim', 3)
('Allo', 2)
('Car', 2)
('Winny', 2)
('Ball', 1)
('Char', 1)
"""