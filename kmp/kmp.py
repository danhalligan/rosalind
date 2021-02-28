#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import GC
import numpy as np
import sys

file = sys.argv[1]
file = "test.txt"
seq = list(SeqIO.parse(file, "fasta"))[0].seq

p = [0]
k = 1
count = 0
while k < len(seq):
    if seq[k] == seq[count]:
        count += 1
        p.append(count)
        k += 1
    else:
        if count > 0:
            count = 0
        else:
            p.append(0)
            k += 1
