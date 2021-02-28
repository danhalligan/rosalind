#!/usr/bin/env python3

import fileinput
import re

for seq in fileinput.input():
    seq = seq.rstrip()[::-1]
    print(seq.translate(str.maketrans("ACGT", "TGCA")))
