#!/usr/bin/env python3

import sys

f = open(sys.argv[1], "r")
l = f.readlines()
print(sum(xi != yi for xi, yi in zip(l[0], l[1])))
