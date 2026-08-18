import json

# Из файла
with open('./json/objs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # загружаем в словарь/список

# Из строки
json_string = '{"name": "Анна", "age": 25}'
data = json.loads(json_string)
print(data['name'])  # Анна

json_string = """[
  {
    "id": 12,
    "name": "Федоров"
  },
  {
    "id": 8,
    "name": "Петров"
  }
]"""
data = json.loads(json_string)
print(data[0]['name'])  # Федоров

# - - - - - - - - - - - - - -

import json

data = {
    "name": "Анна",
    "age": 25,
    "hobbies": ["reading", "swimming"]
}

with open('./json/output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

json_string = json.dumps(data, indent=4, ensure_ascii=True)
print(json_string)
"""
{
    "name": "\u0410\u043d\u043d\u0430",
    "age": 25,
    "hobbies": [
        "reading",
        "swimming"
    ]
}
"""