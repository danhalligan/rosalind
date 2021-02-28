#! /usr/local/bin/Rscript

options(scipen = 999)

n <- 80
m <- 18

v <- c(1, rep(0, m - 1))

for (i in 2:n) {
    v <- c(sum(v[-1]), v[1:(m - 1)])
}
print(sum(v))
