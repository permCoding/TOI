from csv import reader, writer
import sys


def get_date(filename, sep=','):
    lst = []
    with open(filename, 'r', encoding="utf8") as f:
        _reader = reader(f, delimiter=sep)
        headers = next(_reader)  # читаем строку заголовков
        # print(headers)
        for obj in _reader:
            lst.append(obj)
    return lst


def get_update(lst):
    lst_update = []
    for obj in lst:
        new_obj = [
            int(obj[0]), 
            obj[1], 
            int(obj[3])+int(obj[4])+int(obj[5])
        ]
        lst_update.append(new_obj)
    return lst_update


def create_csv(filename, lst, titles, sep=","):
    with open(filename, "w", encoding="utf8", newline="") as f:
        _writer = writer(f, delimiter=sep)
        _writer.writerow(titles)  # записать строку заголовков
        _writer.writerows(lst)  # записать все строки с данными


args = sys.argv

file_in = "./csv/exam_balls.csv"
file_out = "./csv/exam_update.csv"

abits = get_date(file_in, ';')
# for abit in abits: print(abit)

lst_update = get_update(abits)
# lst_update.sort(key=lambda x: -x[2])  # только для числовых данных
lst_update.sort(key=lambda x: x[2], reverse=True)
# for abit in lst_update: print(abit)

cnt = len(lst_update) if (len(args) == 1 or int(args[1]) > len(lst_update)) else int(args[1])
headers = ['id', 'name', 'fullBall']
create_csv(file_out, lst_update[:cnt], headers)

print(f"Записано {cnt} абитуриентов.")
