import math

lst1 = [2/6, 1/6, 3/6]  # => 1.459
lst2 = [2/6, 2/6, 2/6]  # => 1.585


sm = sum(- p * math.log2(p) for p in lst1)
print(f"{sm:.3f}")

sm = sum(- p * math.log2(p) for p in lst2)
print(f"{sm:.3f}")
