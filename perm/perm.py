#!/usr/bin/env python3

from itertools import permutations  
  
n = 5
perm = list(permutations(range(1, n+1)))

print(len(perm))
for i in list(perm):
    print(*i)
