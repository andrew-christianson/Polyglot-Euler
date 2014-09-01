f = (x,n) -> (x^2 - 1) % n
println(f(3, 5))

function gcd(a,b)
	while b != 0
		a, b = b, (a % b)
	end
	a
end


function pollardrho(n)
	f = (x,n) -> (x^2 - 1) % n
	x, y, d = 2, 2, 1
	while d == 1
		x = f(x,n)
		y = f(f(y,n),n)
		d = gcd(abs(x-y), n)
	end
	d
end