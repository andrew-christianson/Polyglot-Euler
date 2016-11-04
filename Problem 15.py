from __future__ import print_function, division
from operator import mul
from functools import reduce
import gmpy
import sys


# Borrowed from scipy/lib/six.py (sort of)
if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range


def bin_coef_sum(n):
    return sum(gmpy.comb(n, i) ** 2 for i in xrange(n+1))


def central_bin_coef(n):
    return gmpy.fac(2 * n) // gmpy.fac(n) ** 2

if __name__ == '__main__':
    print("The Answer to Euler Problem 15 is", central_bin_coef(20))
