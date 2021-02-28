# transition probabilities
f <- matrix(c(0.5, 0.5, 0, 0.25, 0.5, 0.25, 0, 0.5, 0.5), ncol = 3, byrow = TRUE)
rownames(f) <- c("AA", "Aa", "aa")

# start frequencies
v <- c(0, 1, 0)

# After 1 generation (0.5 are hets)
v <- colSums(v*f)
v

# After 2 generations (0.5 are hets)
v <- colSums(v*f)
v

# So after each generation, 0.5 are always hets
# With 2 alleles, 0.25 will be AaBb (by independence)

# After k generations we will have 2^k individuals
# Prob that each individual is AaBb 0.25
# Prob that at least n are AaBb is given by binomial dist with p = 0.25
k <- 7
n <- 36
1 - pbinom(n-1, 2^k, 0.25)

