# f = (x,n) -> (x^2 - 1) % n
# println(f(3, 5))

# function gcd(a,b)
# 	while b != 0
# 		a, b = b, (a % b)
# 	end
# 	a
# end


# function pollardrho(n)
# 	f = (x,n) -> (x^2 - 1) % n
# 	x, y, d = 2, 2, 1
# 	while d == 1
# 		x = f(x,n)
# 		y = f(f(y,n),n)
# 		d = gcd(abs(x-y), n)
# 	end
# 	d
# end

function isprime(n)
	if n & 1 == 0
		return false
	end
	for i = 3:sqrt(n)
		if n % i == 0
			return false
		end
	end
	return true
end


N = 600851475143
largest_factor = 0

for candidate = 3:convert(Int64, ceil(sqrt(N)))
	if N % candidate == 0 
		if isprime(candidate)
			largest_factor = candidate
		elseif isprime(convert(Int64, N / candidate))
			largest_factor = convert(Int64, N / candidate)
		end
	end
end
println("The answer to Euler Problem 3 is $largest_factor")