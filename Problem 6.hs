res :: Integer
main :: IO()

res =  (sum [1..100] ^ 2) - (sum [x ^ 2 | x <- [1..100]])
main = print ("The answer to Euler Problem 6 is " ++ show res)