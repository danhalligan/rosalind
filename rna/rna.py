#!/usr/bin/env python3

import fileinput
import re

for seq in fileinput.input():
    print(re.sub("T", "U", seq.rstrip()))
