"""
из лог файла выбрать строки только с POST запросами
и вывести на экран json структурированно с отступами
массив объектов с полями ip, method, date, time, status, пример:
[
    {
        "ip": "192.168.1.1",
        "date": "10/Oct/2026",
        "time": "13:55:37",
        "method": "POST /api",
        "status": 403
    },
    {
        "ip": "192.168.1.2",
        "date": "10/Oct/2026",
        "time": "13:58:07",     
        "method": "POST /api",
        "status": 404
    }
]
"""

import re, json

log_lines = []
with open('./data/log.log', 'r', encoding='utf8') as f:
    for line in f:
        if line:
            log_lines.append(line)

# 192.168.1.2 - - [10/Oct/2026:13:55:37 +0000] "POST /api" 404 512
pattern = r'([0-9]{1,3}(\.[0-9]{1,3}){3}) .*?\[(.*?)\] "((POST)(.*?))" (\d+)'
for line in log_lines:
    match = re.search(pattern, line)
    if match:
        tpl = match.groups()
        print(tpl)

# # регулярное выражение для извлечения IP, метода, статуса
# pattern = r'(\d+\.\d+\.\d+\.\d+) .*? "(.*?)" (\d+)'
# # pattern = r'([0-9]{1,3}(\.[0-9]{1,3}){3}) .*? "(.*?)" (\d+)'
# parsed = []
# for line in log_lines:
#     match = re.search(pattern, line)
#     if match:
#         ip, method, status = match.groups()
#         # ip, _, method, status = match.groups()
#         res = { "ip": ip, "method": method, "status": int(status) }
#         parsed += [ res ]
# print(json.dumps(parsed, indent=4))

# """
# [
#     {
#         "ip": "192.168.1.1",
#         "method": "GET /index.html",
#         "status": 200
#     },
#     {
#         "ip": "192.168.1.2",
#         "method": "POST /api",
#         "status": 404
#     }
# ]
# """
