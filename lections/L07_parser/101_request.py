import requests  # pip install requests


url = "http://perm.1gb.ru/parsing/rating.html"

userAgent = "Chrome/151.0.0.0"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
userAgent = "MyBot/1.0 (https://my-site.com; my-email@ya.ru)"

headers = { "User-Agent": userAgent }

response = requests.get(url, headers=headers)
response.encoding = "utf8"

# print(response.text)

with open("./data/rating.html", "w", encoding="utf8") as f:
    f.write(response.text)





# ver 1 => просто циклом
# ver 2 => регулярками
# <small>24.03.2026</small> re = r'<small>\s*\d{2}\.\d{2}\.\d{4}\s*</small>'
# ver 3 => с использованием bs4
# если html не отдаётся, тогда надо использовать selenium