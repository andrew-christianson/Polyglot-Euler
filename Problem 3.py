from __future__ import print_function, division
import math
import sys
import numpy

# Borrowed from scipy/lib/six.py (sort of)
if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range


def eratosthenes(ub):
    plist = []
    for candidate in range(2, max(3,ub)):
        fact_ub = math.sqrt(candidate)
        for prime in plist:
            if prime > fact_ub:
                plist.append(candidate)
                yield candidate
                break
            if candidate % prime == 0:
                break
        else:
            plist.append(candidate)
            yield candidate

def smallest_prime_factor(n):
    for prime in eratosthenes(math.ceil(math.sqrt(n))):
        if n % prime == 0:
            return prime
    else:
        return int(n)

def prime_factorization(n):
    pfactors = []
    cur_n = n
    while cur_n > 1:
        pfactors.append(smallest_prime_factor(cur_n))
        cur_n /= pfactors[-1]
    return pfactors

if __name__ == '__main__':
    largerst_pfactor = max(prime_factorization(600851475143))
    print("The answer to Euler Problem 3 is", largerst_pfactor)