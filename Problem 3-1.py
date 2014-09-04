from __future__ import print_function, division
import math
import sys
import gmpy

# Borrowed from scipy/lib/six.py (sort of)
if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range


class Eratosthenes(object):
    plist = [2]
    pset = set()

    def __init__(self, ub):
        self.ub = ub

    def __call__(self):
        if len(self.plist) > 0:
            for item in self.plist:
                yield item
        for candidate in range(self.plist[-1], max(3, self.ub)):
            fact_ub = math.sqrt(candidate)

            for prime in self.plist:
                if prime > fact_ub:
                    self.plist.append(candidate)
                    self.pset.add(candidate)
                    yield candidate
                    break
                if candidate % prime == 0:
                    break
            else:
                self.plist.append(candidate)
                self.pset.add(candidate)
                yield candidate


def smallest_prime_factor(n):
    for prime in Eratosthenes(math.ceil(math.sqrt(n)))():
        if n % prime == 0:
            return prime
    else:
        return int(n)


def prime_factorization(n):
    pfactors = []
    cur_n = gmpy.mpz(n)
    while cur_n > 1:
        pfactors.append(smallest_prime_factor(cur_n))
        cur_n /= pfactors[-1]
    return pfactors


if __name__ == '__main__':
    largerst_pfactor = max(prime_factorization(6008514751437777))
    print("The answer to Euler Problem 3 is", largerst_pfactor)