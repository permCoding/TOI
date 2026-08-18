import csv


filename = "./csv/exam_balls.csv"

with open(filename, 'r', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=";")
    reader.__next__()
    for obj in reader:
        new_obj = []
        for i in range(len(obj)):
            if i == 0:
                new_obj += [obj[i].ljust(3, " ")]
            elif i == 1:
                new_obj += [obj[i].ljust(16, " ")]
            else:
                new_obj += [obj[i] ]
        print(*new_obj, sep=' | ')





    # lst = list(reader)[1:]  # убираем строку заголовков
    # t = sorted(lst, key=lambda x: x[1])
    # for elm in t: print(*elm)
    
    # генератор или итератор
    # lst = [item for item in lst if len(item) > 0]
    # iterator = filter(lambda item: len(item)>0, lst)
    
    # for item in sorted(iterator, key=lambda x: x[1])[:5]:
    #     print(item)
