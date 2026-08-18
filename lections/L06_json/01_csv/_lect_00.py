import csv

filename = './csv/abiturs.csv'

# Чтение как обычный txt
with open(filename, 'r', encoding='utf-8') as f:
    for row in f:
        print(row.split(','))

# Чтение в список списков
with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Чтение в список словарей
with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# - - - - - - - - - - - - 

import csv

data = [
    ['Анна', 25, 'Москва'],
    ['Борис', 30, 'СПб']
]

with open('./csv/output_0.csv', 'w', encoding='utf-8', newline='') as f:
    f.write('name,age,city\n')  # заголовок
    for row in data:  # строки данных
        f.write(','.join(str(item) for item in row) + '\n')

with open('./csv/output_1.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])  # заголовок
    writer.writerows(data)

data = [
    {'name': 'Анна', 'age': 25, 'city': 'Москва'},
    {'name': 'Борис', 'age': 30, 'city': 'СПб'}
]

with open('./csv/output_2.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    writer.writeheader()
    writer.writerows(data)

