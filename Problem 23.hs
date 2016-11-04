factors :: Integer -> [(Integer, Integer)]
abundant :: Integer -> Bool
abundants :: Integer -> [Integer]
abundants_list :: [Integer]
intsToRoot :: Integer -> [Integer]
main :: IO()
is_sum :: Integer -> Integer -> Integer -> Bool
flrt :: Integer -> Integer  -- flrt x ≈ √x,  with  flrt x^2 ≤ x < flrt(x+1)^2
flrt2 :: Integer -> Integer  -- flrt x ≈ √x,  with  flrt x^2 ≤ x < flrt(x+1)^2
--flrt2 :: (Integral c, Integral a) => a -> c
flatten :: [(Integer, Integer)] -> [Integer]
is_sum_in_list :: Integer -> [(Integer, Integer)] -> Bool

sum_of_abund_bool :: [Bool]

flatten [] = []
flatten (x:l) = fst x:(snd x:flatten l)

abundant n = (sum.flatten.factors) n > n
abundants n = takeWhile (<n) [i | i <- [1..], abundant i]
is_sum a b n = a + b == n
is_sum_in_list n l = elem True [is_sum a b n | (a, b) <- l]
flrt2 = floor . sqrt . fromIntegral

--http://stackoverflow.com/a/10865580
flrt x = approx (round . (sqrt::Double->Double) . fromInteger $ x)
   where approx r
            | ctrl <= x, (r+1)^2 > x  = r
            | otherwise               = approx $ r - diff
          where ctrl = r^2
                diff = (ctrl - x) // (2*r)    -- ∂/∂x x² = 2x

         a//b = a`div`b + if (a>0)==(b>0) then 1 else 0   -- always away from 0


intsToRoot n =  takeWhile (<= flrt2 n) [1..]  
factors n = [(i, quot n i) | i <- intsToRoot n, mod n i == 0]

abundants_list = abundants 28200
abundants_prod_list = cartProd abundants_list abundants_list
sum_of_abund_bool = [is_sum_in_list i abundants_prod_list | i <- [1..100]]

main = print (sum [1 | i <- sum_of_abund_bool, i == True])
cartProd xs ys = [(x,y) | x <- xs, y <- ys]
