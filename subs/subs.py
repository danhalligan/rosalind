#!/usr/bin/env python3

import sys

def subs(seq1, seq2):
    size = len(seq2)
    for i in range(len(seq1) - size + 1):
        if seq1[i:(i+size)] == seq2:
            yield i + 1

f = open(sys.argv[1], "r")
seqs = f.read().splitlines()
print(*list(subs(seqs[0], seqs[1])))

