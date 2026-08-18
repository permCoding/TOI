def save_to_csv(lst, filename, sep=','):
    with open(filename, "w", encoding="utf-8") as f:
        lines = []
        for obj in sorted(lst, key=lambda e: e[1]):
            lines += [sep.join(str(elm) for elm in obj) + "\n"]
        f.writelines(lines)


userA = "1, Мишкин, 217, 1, 2002-08-23, Кунгур"
userB = "202, Бортич, 224, 0, 2002-06-03, Лысьва"
userC = "33, Кротов, 217, 1, 2002-07-13, Кунгур"
users = [userA, userB, userC]


fn = "./csv/task_01.csv"
save_to_csv(users, fn, " ")

"""
1) из строк сделать объекты типа user в виде таких списков [,,,,,]
2) выбрать только тех кто из Кунгура
3) убрать поле Дата рождения
4) сортировать по убываниюб рейтинга
5) сохранить в файл "./csv/task_01.csv"
"""
