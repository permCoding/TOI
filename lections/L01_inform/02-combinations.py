import itertools

for amount in range(10, 101, 10):
    rng = range(1, amount+1)
    combinations = list(itertools.combinations(rng, 2))

    print(amount, len(combinations))
    # print(combinations)
"""
pairs = n * (n-1) / 2

10 45
20 190
30 435
40 780
50 1225
60 1770
70 2415
80 3160
90 4005
100 4950

3 3
4 6
5 10
6 15
7 21
8 28
9 36
10 45
11 55
12 66
13 78
14 91
15 105
16 120
17 136
18 153
19 171
20 190
21 210
22 231
23 253
24 276
"""