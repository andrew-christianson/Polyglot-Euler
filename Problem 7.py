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


class Eratosthenes(object):
    plist = [2]

    def __init__(self, ub):
        self.ub = ub

    def __call__(self):
        if len(self.plist) > 0:
            for item in self.plist:
                yield item
        for candidate in range(self.plist[-1], max(3, self.ub)):
            # if (candidate & 1 != 0): continue
            fact_ub = math.sqrt(candidate)

            for prime in self.plist:
                if prime > fact_ub:
                    self.plist.append(candidate)
                    yield candidate
                    break
                if candidate % prime == 0:
                    break

if __name__ == '__main__':
    for idx, prime in enumerate(Eratosthenes(1000000000)()):
        if idx == 10001:
            break
    print("The answer to Euler Problem 7 is", prime)