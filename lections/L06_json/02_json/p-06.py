import requests, json
from my_module import obj_update


user = 'permCoding'
url = f'https://api.github.com/users/{user}/repos'
repsonse = requests.get(url)
repsonse.encoding = "utf8"

lst = repsonse.json()
lang = "Python"  # "JavaScript" 

filtred = filter(lambda elm: elm['language'] == lang, lst)  # WHERE

updated = sorted(
    map(lambda obj: obj_update(obj), filtred),
    key=lambda elm: elm['name'],
    reverse=False
)  # [:3]

print(json.dumps(updated, indent=4))

with open('./json/github.json', 'w', encoding='utf8') as f:
    json.dump(updated, f, ensure_ascii=False, indent=4)

# reduce()