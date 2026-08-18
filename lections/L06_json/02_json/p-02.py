import requests, json


user = 'permCoding'
url = f'https://api.github.com/users/{user}/repos'
repsonse = requests.get(url)
repsonse.encoding = "utf8"

lst = repsonse.json()  # ===

print(len(lst))
owner = lst[0]['owner']
print(json.dumps(owner, indent=4))

url_f = owner['followers_url']
repsonse = requests.get(url_f)
repsonse.encoding = "utf8"
lst = repsonse.json()  # ===
print(len(lst))
