import csv
import json


filename = "./csv/abiturs.csv"

with open(filename, "r", encoding="utf8") as f:
    reader = csv.DictReader(f, delimiter=",")
    rows = list(reader)
    # print(rows[0])
    # print(list(rows[0].keys()))

    headers = list(rows[0].keys())
    with open("./csv/result.csv", "w", encoding="utf8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()  # заголовки

        filtred = filter(lambda x: x["city"] == "Кунгур", rows)
        for ab in sorted(filtred, key=lambda x: x["rating"], reverse=True):
            writer.writerow(ab)  # данные
