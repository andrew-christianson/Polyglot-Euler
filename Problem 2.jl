function fib(max_val)
	res, val, i_m2 = 0, 0, 0
	i_m1 = 1

	while val < max_val
		val = i_m1 + i_m2
		i_m1, i_m2 = val, i_m1
		((val & 1) == 0) && (res += val)
	end 
	println("The imperative answer to Euler Problem 2 is $res")
end

@time fib(4000000)

function fibarr(max_val, )
	arr = [1,1]
	# println(arr)
	while arr[end] < max_val
		arr = [arr, arr[end]+arr[end-1]]
	end
	arr
end

@time (farr = fibarr(4000000);
       res2 = +(filter(x -> x & 1 == 0, farr)...))

println("The slightly more idiomatic answer to Problem 3 is $res2")

