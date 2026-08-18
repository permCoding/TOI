import requests
import json

prodFindEncoded = 'notebook'
page = 1

host = f'https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search'
query = f'ab_testing=false&ab_testing=false&appType=1&curr=rub&dest=-1581744&hide_dtype=9;11&hide_vflags=4294967296&inheritFilters=false&lang=ru&page=${page}&query=${prodFindEncoded}&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false'

url = host + '?' + query

headers = {
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9",
    "deviceid": "site_60cbc695c06243b9bfdcd03c1db06c9e",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"YaBrowser\";v=\"25.10\", \"Yowser\";v=\"2.5\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-queryid": "qid521791226175438496120251208085958",
    "x-requested-with": "XMLHttpRequest",
    "x-spa-version": "13.16.1",
    "x-userid": "0",
    "cookie": "_wbauid=5217912261754384961; x_wbaas_token=1.1000.6ad288dede4b4303ac6f8756c0bff7af.MHwxNzguMTc4LjIzNy4yMTd8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0MC4wLjAuMCBZYUJyb3dzZXIvMjUuMTAuMC4wIFNhZmFyaS81MzcuMzZ8MTc2NjM5Mzk4M3xyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3NjU3ODkxODN8MQ==.MEQCIEFZSq18HxZdmCxxxwbzYrgWT2pIB00+B7+HdolDkZVkAiB8ycbxcRzl9q8wsp66QcMVwZ6L1xskDxwazN7rZXnPlQ==; _cp=1",
    "Referer": "https://www.wildberries.ru/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf8"
print(response.text)
# print(response.json)
# dataJSON = json.loads(response.text)  # строку в объект
# print(dataJSON)

# s = json.dumps(dataJSON, ensure_ascii=False, indent=4)

# print(s)
