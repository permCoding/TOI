import json


fl = '2024'
with open("./json/github.json", "r", encoding="utf-8") as f:
    print(
        json.dumps(
            [obj for obj in json.load(f) if obj['created_at'].split('-')[0] == fl], 
            indent=4, 
            ensure_ascii=False
        )
    )
