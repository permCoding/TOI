symbols = 'Python'


codes = [ord(symbol) for symbol in symbols]  # listcomp
print(codes)  # [80, 121, 116, 104, 111, 110]


dct = {symbol:ord(symbol) for symbol in symbols}
print(dct)
# {'P': 80, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

# genexp - это в круглых скобках - итератор

coords_X, coords_Y = (0,1,2), (0,1,2)
w = ((x,y) for x in coords_X for y in coords_Y)
print(w)  # <generator object <genexpr> at 0x0000023D5B06C820>
for pair in w:
    x, y = pair
    dist = (x**2 + y**2)**.5
    print(f'X = {x}; Y = {y}; dist = {dist:.2f}')

X = 0; Y = 0; dist = 0.00
X = 0; Y = 1; dist = 1.00
X = 0; Y = 2; dist = 2.00
X = 1; Y = 0; dist = 1.00
X = 1; Y = 1; dist = 1.41
X = 1; Y = 2; dist = 2.24
X = 2; Y = 0; dist = 2.00
X = 2; Y = 1; dist = 2.24
X = 2; Y = 2; dist = 2.83