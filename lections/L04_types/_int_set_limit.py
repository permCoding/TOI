import sys

sys.setrecursionlimit(2200)
sys.set_int_max_str_digits(6000)

def f(n):
    if n > 1:
        return (n-1)*f(n-1)
    else:
        return 1
    
result = f(2026)
print( len(str(result)) )  # 5819

# sys.setrecursionlimit(4000)
# sys.set_int_max_str_digits(8000)

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return (n-1)*f(n-1)
    
# print( (f(2024)-3*f(2023)) / f(2022) )  # 4084440