lst = [chr(0x1f600), chr(128194)]  # '😀' '📂'
print(lst)  # ['😀', '📂']



for smb in lst:
   _ord = ord(smb)  # print(f"{_ord:04X})
   _smb = bin(_ord)[2:].zfill(21)
   # _smb = f"{_ord:021b}"
   bt1 = int('11110' + _smb[0:3], 2)
   bt2 = int('10' + _smb[3:9], 2)
   bt3 = int('10' + _smb[9:15], 2)
   bt4 = int('10' + _smb[15:21], 2)
   utf8_bytes = bytes([bt1, bt2, bt3, bt4])
   print(smb, utf8_bytes.decode('utf-8'))

   print(f"UTF-8 байты (hex): {' '.join(f'{b:02x}' for b in utf8_bytes)}")
   print(utf8_bytes.decode('utf-8'))
   print(smb.encode('utf-8'))
   
   # URL-кодировка (percent-encoding)
   from urllib.parse import quote, unquote
   encoded = quote(smb)  # '%F0%9F%98%80'
   print(encoded)
   decoded = unquote(encoded)  # '😀' - # Декодирование обратно
   print(decoded)
   
"""
😀 😀 1F600
📂 📂 1F4C2
"""
