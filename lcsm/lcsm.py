#!/usr/bin/env python3

from Bio import SeqIO
import sys

file = "rosalind_lcsm.txt"
seqs = list(SeqIO.parse(file, "fasta"))
seqs = [x.seq for x in sorted(seqs, key = len)]

maxsub = ''
s0 = seqs.pop()
s = len(s0)

# brute force
for i in range(s):
    for j in range(i+len(maxsub), s):
        for seq in seqs:
            if s0[i:j] not in seq:
                break
        else:
            maxsub = s0[i:j]

print(maxsub)
