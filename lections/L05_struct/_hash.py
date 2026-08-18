print(hash('ABC'))     # 1433972551973331715
print(hash('Python'))  # 2068729341365198690

# такие хэши будут отличаться в разных запусках программы
# такой хэш может быть отрицательным
# хэши не декодируются обратно в строку
# не все объекты являются хэшируемыми в смысле hash()


import hashlib
# такие хэши будут одинаковыми в каждом запуске программы

bt = bytes("пароль", encoding='utf-8')
hs1 = hashlib.md5(bt)
print(hs1)  # <md5 _hashlib.HASH object @ 0x0000028CC78ADB90>
to_saved_1 = hs1.hexdigest()
print(to_saved_1)  # e242f36f4f95f12966da8fa2efd59992


bt = b"password"
hs2 = hashlib.md5(bt)
print(hs2)  # <md5 _hashlib.HASH object @ 0x0000028CC78AE030>
to_saved_2 = hs2.hexdigest()
print(to_saved_2)  # 5f4dcc3b5aa765d61d8327deb882cf99


input = "пароль"
hs1 = hashlib.md5(bytes(input, encoding='utf-8'))
print(to_saved_1 == hs1.hexdigest())

input = "password"
hs2 = hashlib.md5(bytes(input, encoding='utf-8'))
print(to_saved_2 == hs2.hexdigest())
