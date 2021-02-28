iprb <- function(k, m, n) {
    tot <- choose(k + m + n, 2)
    poss <-
        choose(k, 2) +      # dom with dom
        k*m +               # dom with het
        k*n +               # dom with rec
        m*n * 1/2 +           # het with rec
        choose(m, 2) * 3/4  # het with het
    poss/tot
}

iprb(2, 2, 2)
iprb(20, 19, 26)
