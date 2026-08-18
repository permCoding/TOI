from bs4 import BeautifulSoup

with open('./data/rating.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# нашли первый
_first = soup.find('td', class_='surname')

# ищем следующий в том же родителе
if _first:  # Иванов:
    print(_first.text.strip())  # Петров
    _next = _first.find_next('td', class_='surname')
    if _next:
        print(_next.text.strip())  # Петров

while _next:  # и все остальные
    _next = _next.find_next('td', class_='surname')
    if _next:
        print(_next.text.strip())  # Петров
    else:
        break
        

