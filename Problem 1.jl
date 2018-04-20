mults = [1:1000]
@time  res = +(filter(x -> (x % 3 == 0) | (x % 5 == 0), mults)...)
res = 0
@time for m in mults
    if (m % 3 == 0) | (m % 5 == 0)
        res += m
    end
end    
println("The answer to Euler Problem 1 is $res")

