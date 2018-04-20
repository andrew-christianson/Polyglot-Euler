mults = 1:1000
res = sum(mults[(mults %% 3 == 0) | (mults %% 5 == 0)])
cat("The answer to Euler Problem 1 is ")
cat(res)
cat("\n")


test <- data
