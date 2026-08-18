# ver 3 => с использованием bs4
from bs4 import BeautifulSoup  # pip install bs4

with open('./data/rating.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1 - найти все ячейки с Фамилиями
surnames = soup.find_all('td', class_='surname')  # 1
surnames = soup.select('td.surname')              # 2
surnames = soup.select('.surname')                # 3
surnames = soup.find_all('td', attrs={'class': 'surname'})  # 4

# 2 - достать все Фамилии
surnames = [tag.get_text(strip=True) for tag in surnames]
surnames = [tag.get_text().strip() for tag in surnames]
surnames = [tag.text.strip() for tag in surnames]  # ~ .get_text()

print(len(surnames), sorted(surnames))

# 2 - Найти все строки таблицы (кроме заголовка)
# table = soup.find('table')
# table = soup.find(id='table-rating')

# if table: tbody = table.find('tbody')
# if tbody: 
#     rows = tbody.find_all('tr')
# else:
#     rows = []
# if table: rows = soup.select('tbody tr')
# rows = soup.select('tbody tr')
# print(len(rows))



# for row in rows:
#     cells = row.find_all('td')
#     number = cells[0].text
#     surname = cells[1].text
#     score = cells[2].text
#     print(f"{number:>3} {surname:<12} {score:>5}")
    
# lst = []
# for row in rows:
#     cells = row.find_all('td')
#     number = int(cells[0].text)
#     surname = cells[1].text
#     score = int(cells[2].text)
#     abit = (number, surname, score)
#     lst.append( abit )
# lst.sort(key=lambda tpl: -tpl[2])
# for elm in lst:
#     number, surname, score = elm
#     print(f"{number:>3} {surname:<12} {score:>5}")