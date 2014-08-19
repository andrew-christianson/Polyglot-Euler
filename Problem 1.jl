mults = [1:1000]
res = +(filter(x -> (x % 3 == 0) | (x % 5 == 0), mults)...)
println("The answer to Euler Problem 1 is $res")