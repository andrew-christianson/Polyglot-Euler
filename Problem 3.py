from __future__ import print_function, division
import math
import sys

# Borrowed from scipy/lib/six.py (sort of)
if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range


def isprime(num):
    if num == 2:
        return True
    bound = int(math.ceil(math.sqrt(num)))
    for cfactor in xrange(2, bound):
        if num % cfactor == 0:
            return False
    return True

if __name__ == '__main__':
    N = 600851475143
    factors = [
            [f, N // f] 
            for f in xrange(3,int(math.ceil(math.sqrt(N))))
            if (N % f) == 0
            ]
    factors = sum(factors, [])
    factors = [f for f in factors if isprime(f)]
    print("The answer to Euler Probelm 3 is", max(factors))
