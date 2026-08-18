import yaml  # pip install pyyaml

data = {
    "name": "Анна",
    "age": 25,
    "hobbies": ["reading", "swimming"]
}

# with open('./data/output.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

"""
age: 25
hobbies:
- reading
- swimming
name: Анна
"""

with open('./data/output.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(data)
# {'age': 25, 'hobbies': ['reading', 'swimming'], 'name': 'Анна'}