import re


txt = "000abc000"

ptn = re.compile(r'abc')
m = ptn.search(txt)
if m:
    print(m)  # <re.Match object; span=(3, 6), match='abc'>
    print(m.group())  # abc
    print(m.span())   # (3, 6)
    print(m.start())  # 3
    print(m.end())    # 6

m = re.search(r'abc', txt, re.I)
if m:
    print(m)  # <re.Match object; span=(3, 6), match='abc'>
    print(m.group())  # abc
    print(m.span())   # (3, 6)
    print(m.start())  # 3
    print(m.end())    # 6
