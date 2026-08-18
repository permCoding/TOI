data = [True, False, True, True, False]
count_true = sum(data)  # 3
print(count_true)

lst = [1,12,2,4,9,4,3]
sm = sum(e%3==0 for e in lst)
print(sm)  # 3