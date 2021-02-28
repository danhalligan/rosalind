#!/usr/bin/env python3

import fileinput

for seq in fileinput.input():
    print(*(seq.count(nuc) for nuc in 'ACGT'))
