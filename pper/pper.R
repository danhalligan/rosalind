n <- 98
k <- 9

Reduce(function(p, i) (p * i) %% 1e6, seq(n, n-k+1, -1))
