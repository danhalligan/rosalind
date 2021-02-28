#!/usr/bin/env python3

from Bio import SeqIO
import sys

def revp(seq):
    for size in range(4, 13):
        for i in range(len(seq) - size + 1):
            subseq = seq[i:(i+size)]
            rev = subseq.reverse_complement()
            if rev.seq == subseq.seq:
                yield [i + 1, size]


file = sys.argv[1]
seq = list(SeqIO.parse(file, "fasta"))[0]
res = list(revp(seq))
res.sort()
[print(*row, sep=' ') for row in res]

