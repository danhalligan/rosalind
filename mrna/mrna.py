#!/usr/bin/env python 3

from functools import reduce

codons = {
    'F': 2,
    'L': 6,
    'I': 3,
    'M': 1,
    'V': 4,
    'S': 6,
    'P': 4,
    'T': 4,
    'A': 4,
    'Y': 2,
    'H': 2,
    'Q': 2,
    'N': 2,
    'K': 2,
    'D': 2,
    'E': 2,
    'C': 2,
    'W': 1,
    'R': 6,
    'G': 4,
    '*': 3
}

file = open("rosalind_mrna.txt", "r")
seq = file.readline().split()[0] + '*'
reduce(lambda p, c: p*codons[c] % 1000000, seq, 1)
