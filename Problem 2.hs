-- Slow naive fib
--fib 0 = 0
--fib 1 = 1
--fib n = fib (n-1) + fib(n-2)

-- fast memo'd fib from http://www.haskell.org/haskellwiki/Memoization
memoizedFib :: Int -> Integer
res :: Integer
main :: IO()

memoizedFib = (map fib [0 ..] !!)
   where fib 0 = 0
         fib 1 = 1
         fib n = memoizedFib (n-2) + memoizedFib (n-1)

res = sum  [y | y<-takeWhile (<4000000) [memoizedFib x | x <- [1..]], y `mod` 2 == 0]

main = print ("The answer to Euler Problem 2 is " ++ show res)