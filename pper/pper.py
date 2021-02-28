from functools import reduce

n = 98
k = 9

reduce(lambda p, i: int((p * i) % 1e6), range(n, n-k, -1))
