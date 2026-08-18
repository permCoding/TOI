x = 1024
s = str(x)

print(s[0], s[-1])  # 1 4
print(s[::-1])  # 4201

# заменить символ в строке
# s[0] = 9  # не работает

s = '9' + s[1:]
print(s)

lst = list(s)
lst[0] = '9'
s = ''.join(lst)
print(s)
