fib <- function(max){
	fibarr <- c(1,1)
	while (tail(fibarr, n=1) < max) {
		fibarr <- c(fibarr, sum(tail(fibarr, n=2)))
	}
	return(fibarr)
}	

fa <- fib(4000000)
res <- sum(fa[fa %% 2 == 0])
print(paste("The answer to Euler Problem 2 is ", res, sep=""))