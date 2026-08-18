import timeit

# сравнение bool быстрее, чем сравнение int
def test_bool():
    if True:
        pass

def test_int():
    if 1:
        pass

print(timeit.timeit(test_bool, number=30_000_000))
print(timeit.timeit(test_int, number=30_000_000))
# 0.8588936000014655
# 0.9011865999782458