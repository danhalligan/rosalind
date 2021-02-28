#!/usr/bin/env python3

import fileinput
from Bio.Seq import Seq

for seq in fileinput.input():
    print(Seq(seq.rstrip()).translate())
