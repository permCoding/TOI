# ver 1 => просто циклом

start, end = '<td class="surname">', '</td>'
ln = len('<td class="surname">')

with open('./data/rating.html', 'r', encoding="utf8") as f:
    s = f.read()
    
    pos = 0
    while s.find(start, pos) > -1:
        pos = s.find(start, pos)
        print(pos, s[pos+ln:pos+ln+12])
        # дописать код для извлечения данных
        pos += ln + 12
