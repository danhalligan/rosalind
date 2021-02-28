#!/usr/bin/env python3

import sys
import math

def logp(c, p):
    return math.log10({'G': p, 'C': p, 'A': 1-p, 'T': 1-p}[c] / 2)

file = sys.argv[1]
seq, arr = open(file, "r").read().splitlines()
arr = [float(x) for x in arr.split(' ')]

res = [
    round(sum([logp(c, p) for c in seq]), 3)
    for p in arr
]
print(*res)
