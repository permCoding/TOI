import requests, json


user = 'permCoding'
url = f'https://api.github.com/users/{user}/repos'
repsonse = requests.get(url)
repsonse.encoding = "utf8"

lst = repsonse.json()

# filtred = [elm for elm in lst if elm['language'] == "Python"]

filtred = filter(lambda elm: elm['language'] == "Python", lst)

# lst = list(filtred)
# print(lst[2])

# print(*filtred)  # ...filtred


# list(filter(lambda elm: elm['language'] == "Python", lst))

# jsonData = []
# for elm in filtred:
#     obj = {
#         "id": elm["id"],
#         "private": elm["private"],
#         "name": elm["name"],
#         "url": elm["url"],
#         "language": elm["language"]
#     }
#     jsonData.append(obj)
    
# print(json.dumps(jsonData, indent=4))

# with open('./json/github.json', 'w', encoding='utf8') as f:
#     json.dump(jsonData, f, ensure_ascii=False, indent=4)
