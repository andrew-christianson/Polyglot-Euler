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

class memoize(object):

    def __init__(self, func):
        self.func = func
        self.mdict = {}

    def __call__(self, arg):
        try:
            return self.mdict[arg]
        except KeyError:
            self.mdict[arg] = self.func(arg)
            return self.mdict[arg]

@memoize
def isprime(num):
    if num == 2:
        return True
    bound = math.sqrt(num)
    if num & 1 == 0:
        return False
    for cfactor in xrange(3, int(bound + 1)):
        if num % cfactor == 0:
            return False
    return True

def cfactor(num):
    inum = num
    factors = set()
    while True:
        for fac in xrange(2, int(math.sqrt(num)) + 1):
            if num % fac == 0:
                factors.add(fac)
                factors.add(num)
                continue
        break
    print(sorted(list(factors)))
    return factors

if __name__ == '__main__':
    count = 0
    factors = set([1])
    val = 600851475143
    while True:
        for fac in range(max(factors) + 1, int(math.sqrt(val))):
            if val % fac == 0 and isprime(fac):
                factors.add(fac)
                # print(fac)
        break
    print("The answer to Euler Problem 3 is {}".format(max(factors)))
