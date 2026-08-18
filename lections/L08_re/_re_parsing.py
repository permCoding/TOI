import re, json

log_lines = [
    '192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html" 200 2326',
    '192.168.1.2 - - [10/Oct/2023:13:55:37 +0000] "POST /api" 404 512',
    '192.168.1.2000 - - [10/Oct/2023:13:55:37 +0000] "POST /api" 404 512'
]

# регулярное выражение для извлечения IP, метода, статуса
pattern = r'(\d+\.\d+\.\d+\.\d+) .*? "(.*?)" (\d+)'
# pattern = r'([0-9]{1,3}(\.[0-9]{1,3}){3}) .*? "(.*?)" (\d+)'
parsed = []
for line in log_lines:
    match = re.search(pattern, line)
    if match:
        ip, method, status = match.groups()
        # ip, _, method, status = match.groups()
        res = { "ip": ip, "method": method, "status": int(status) }
        parsed += [ res ]
print(json.dumps(parsed, indent=4))

"""
[
    {
        "ip": "192.168.1.1",
        "method": "GET /index.html",
        "status": 200
    },
    {
        "ip": "192.168.1.2",
        "method": "POST /api",
        "status": 404
    }
]
"""
