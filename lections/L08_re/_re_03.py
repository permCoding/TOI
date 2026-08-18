import re

comp = re.compile(r'abc')

matches = comp.findall('ABC-abc-abc-')
if matches:
    for match in matches:
        print(match)

matches = comp.finditer('ABC-abc-abc-')
if matches:
    for match in matches:
        print(match.group(), match.span())