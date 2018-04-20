import math
import collections
from functools import reduce
from operator import mul


def isprime(num):
    if num == 2:
        return True
    for cfactor in xrange(2, ub(num)):
        if num % cfactor == 0:
            return False
        return True


def ub(num):
    return int(math.ceil(math.sqrt(num)))

def factor(num):
    if num == 2:
        return None
    for f in range(2,ub(num)+1):
        if num % f == 0:
            return [f, num // f]
    return None

def pf(num):
    factors = factor(num)
    if factors:
        return pf(factors[0]) + pf(factors[1])
    else:
        return [num]

def main():
    lf = [pf(f) for f in range(1,20)]
    mm = collections.defaultdict(lambda : 0)
    for fs in lf:
        cs = collections.defaultdict(lambda : 0)
        for f in fs:
            cs[f] += 1
        for f, c in cs.items():
            mm[f] = max(cs[f], mm[f])
    fs = [
            f
            for f, c in mm.items()
            for _ in range(c)
            ]

    print(fs)
    print("The answer to Euler Problem 5 is", 
            reduce(mul, fs, 1))

main()
