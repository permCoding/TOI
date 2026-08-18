import requests  # pip install requests
# import csv  # можно использовать всю библиотеку или выборочно методы из неё
from csv import reader  # библиотека csv входит в Python


# filename = "http://perm.1gb.ru/csv/abiturs.csv"  # адрес файла
filename = "http://files-pcoding.1gb.ru/csv?filename=abiturs.csv"
# filename = "http://files-pcoding.1gb.ru/csv?filename=exam_balls.csv"

response = requests.get(filename)
response.encoding = "utf8"
print(response.text)

f = open("./csv/response.txt", "w", encoding="utf8")
f.write(response.text)
f.close()

# = = = = = = = pause 

# lines = response.text.split("\n")

# # print(lines)
# # for line in lines: print(line)

# with open("./csv/data.csv", "w", encoding="utf8", newline="") as f:
#     for line in lines:
#         f.write(line)

# # = = = 

# # reader = csv.reader(lines, delimiter=",")
# reader = reader(lines)  # delimiter=","

# headers = next(reader)  # читаем строку заголовков
# # print(headers)

# print(f'headers: {", ".join(headers)}')
# for row in reader: print(row)
