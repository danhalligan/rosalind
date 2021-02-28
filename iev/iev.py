#!/usr/bin/env python3

def iev(v):
    p = [1, 1, 1, 0.75, 0.5, 0]
    return sum([x[0]*x[1]*2 for x in zip(v, p)])

f = open("rosalind_iev.txt", "r")
dat = f.readlines()[0].rstrip()
dat = [int(x) for x in dat.split(" ")]

# print(iev([1, 0, 0, 1, 0, 1]))
print(iev(dat))
