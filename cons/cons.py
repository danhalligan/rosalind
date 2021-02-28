#!/usr/bin/env python3

from Bio import SeqIO
import numpy as np
import sys

def count_bases(v):
    return [sum(v == b) for b in 'ACGT']

file = sys.argv[1]
# file = "test.fa"
x =  list(SeqIO.parse(file, "fasta"))
x = np.array([x.seq for x in x])

counts = np.array([count_bases(v) for v in x.T]).T
seq = ['ACGT'[np.argmax(v)] for v in counts.T]

print(''.join(seq))
for i in range(0, 4):
    print('ACGT'[i] + ':', *counts[i])
