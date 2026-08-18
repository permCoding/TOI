import csv


filename = './csv/exam_balls.csv'

with open(filename, "r", encoding="utf8") as f:  
    reader = csv.reader(f, delimiter=";")
    
    headers = next(reader)  # читаем строку заголовков
    print(f'headers => {",".join(headers)}')
    
    # IdStudent,NameStudent,Gender,BallMath,BallLang,BallInf,IdDirect
    # 0         1           2      3        4        5       6
    
    lst = []
    # сделать обычным циклом
    #
    #
    lst = [[item[1], item[2], int(item[3])] for item in reader if item[2] == "м"]
    #       NameStudent, Gender, BallMath
    
    for row in sorted(lst, key=lambda x: -x[2]):  # по убыванию по BallMath
        print(f"{row[2]}\t{row[0]}")

"""
выбрать всех М и отсортировать по убыванию по оценке за математику
"""