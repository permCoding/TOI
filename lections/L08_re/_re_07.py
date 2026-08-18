import re

html = """
<div>
    <a href="https://example.com">Главная</a>
    <a href="/about">О нас</a>
    <a href="/contact">Контакты</a>
    <span>Не ссылка</span>
</div>
"""

# Паттерн с вложенными группами:
# группа 1 — tag <a (весь тег)
# группа 2 — href (ссылка)
# группа 3 — текст внутри тега (содержимое)
comp = re.compile(r'(<a\s+href="([^"]+)"\s*>(.*?)</a>)', re.IGNORECASE)

matches = comp.findall(html)
for tag, href, text in matches:
    print(tag)
    print(f"Текст: {text.strip():<10} → Ссылка: {href}")


for match in comp.finditer(html):
    tag  = match.group(1)     # первая группа: ссылка
    href = match.group(2)     # первая группа: ссылка
    text = match.group(3)     # вторая группа: текст
    print(tag)
    print(f"Текст: {text.strip():<10} → Ссылка: {href}")

"""
<a href="https://example.com">Главная</a>
Текст: Главная    → Ссылка: https://example.com
<a href="/about">О нас</a>
Текст: О нас      → Ссылка: /about
<a href="/contact">Контакты</a>
Текст: Контакты   → Ссылка: /contact
"""
