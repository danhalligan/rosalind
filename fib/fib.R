#! /usr/local/bin/Rscript

inp <- scan("rosalind_fib.txt", integer())
v <- c(0, 1)
n <- inp[1]
k <- inp[2]
out <- replicate(n, v <<- c(v[2], v[1] * k + v[2]))
cat(v[1], "\n")
