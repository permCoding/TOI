# ver 2 => регулярками
# <td class="surname">Иванов</td>
import re


ptn = r'<td class="surname">\s*(\S+)\s*</td>'

with open('./data/rating.html', 'r', encoding="utf8") as f:
    s = f.read()
    for i, match in enumerate(re.findall(ptn, s), start=1):
        print(i, match)

# - - - - - - - - - - - - - 

import re

# компилируем регулярное выражение один раз
pattern = re.compile(r'<td class="surname">\s*(\S+)\s*</td>')

with open('./data/rating.html', 'r', encoding='utf-8') as f:
    s = f.read()
    for i, match in enumerate(pattern.findall(s), start=1):
        print(i, match)