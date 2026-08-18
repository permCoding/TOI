import requests

# url = "https://pcoding.ru/json/clients.json"
url = "http://perm.1gb.ru/json/clients.json"

response = requests.get(url)
response.encoding = "utf8"
line = response.text

print(line)
