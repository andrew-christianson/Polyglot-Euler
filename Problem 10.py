from __future__ import print_function, division
from itertools import count, takewhile
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


class SimpleSieve(object):
    def __iter__(self):
        return self
    def __next__(self):
        for can in count(self.last + 1):
            if self._check(can):
                self.primes.append(can)
                self.last = can
                return can

    def __init__(self):
        self.primes = []
        self.last = 1    
    
    def _check(self, can):
        for prime in self.primes:
            if prime > math.sqrt(can):
                return True
            if can % prime == 0:
                return False
        return True

class Eratosthenes(object):
    def __init__(self, ub):
        self.ub = ub
        self.primes = [2]
        self.candidates = range(3,ub, 2)
        


if __name__ == '__main__':
    primes = [
            prime
            for prime in takewhile(lambda x : x < 2e6, SimpleSieve())
    ]
    print("The answer to Euler Problem 10 is", sum(primes))
