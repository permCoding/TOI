from bs4 import BeautifulSoup

with open('./data/rating.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

_next = soup.find('td', class_='surname')  # первый
while (current := _next) is not None:  # и все остальные
    print(current.text.strip())  # Петров
    _next = current.find_next('td', class_='surname')
        

