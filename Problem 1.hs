--import qualified Data.Set as Set

--threes = Set.fromList [0,3..1000]
--fives = Set.fromList [0,5..1000]

--res = (Set.union threes fives)
--main = putStrLn ("The answer to Euler Problem 1 is " ++ show res)

res :: Integer
main :: IO()

res = sum [x | x<-[0..1000], mod x 3 == 0 || mod x 5 == 0] 
main = print ("The answer to Euler Problem 1 is " ++ show res)
