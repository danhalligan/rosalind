#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import GC
import numpy as np
import sys

x = [rec for rec in SeqIO.parse(sys.argv[1], "fasta")]
gc = [GC(rec.seq) for rec in x]
m = np.argmax(gc)

print(x[m].id)
print(gc[m])
