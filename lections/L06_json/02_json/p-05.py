import requests, json


def obj_update(elm):
    return {
        "id": elm["id"],
        "private": elm["private"],
        "name": elm["name"],
        "url": elm["url"],
        "language": elm["language"]
    }


user = 'permCoding'
url = f'https://api.github.com/users/{user}/repos'
repsonse = requests.get(url)
repsonse.encoding = "utf8"

lst = repsonse.json()
lang = "JavaScript"  # "Python"
# filtred = [elm for elm in lst if elm['language'] == "Python"]

filtred = filter(lambda elm: elm['language'] == lang, lst)  # WHERE

updated = list(map(lambda obj: obj_update(obj), filtred))

print(json.dumps(updated, indent=4))

# with open('./json/github.json', 'w', encoding='utf8') as f:
#     json.dump(updated, f, ensure_ascii=False, indent=4)

# reduce()