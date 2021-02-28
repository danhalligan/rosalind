#!/usr/bin/env python3

from Bio import SeqIO
import sys

def kmp(seq):
    j = -1
    b = [j]
    for i in range(len(seq)):
        while j >= 0 and seq[i] != seq[j]:
            j = b[j]
        j += 1
        b.append(j)
    return b[1:]

seq = list(SeqIO.parse(sys.argv[1], "fasta"))[0].seq
print(*kmp(seq))
