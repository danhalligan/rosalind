#!/usr/bin/env python3

import sys

# divide & conquer
def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b

# recursion
def fib2(n, k):
    if n < 2:
        return n
    return k * fib2(n-2, k) + fib(n-1, k)

# dynamic programming
def fib3(n, k):
    f = [0, 1]

    for i in range(n-1):
        f.append(f[-1] + f[-2] * k)

    return f[-1];

file = open(sys.argv[1], "r")
n, k = map(int, file.readline().split())

print(fib(n, k))
print(fib2(n, k))
print(fib3(n, k))
