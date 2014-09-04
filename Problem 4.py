from __future__ import print_function, division
import sys
import itertools
# Borrowed from scipy/lib/six.py (sort of)
if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range


def is_palindrome(n):
    n = str(n)
    if len(n) & 1 == 0:
        # even # of digits
        mid = int(len(n) / 2)
        return n[:mid] == n[mid:][::-1]
    else:
        # odd # of digits
        mid = int((len(n) // 2) + 1 )
        return n[:mid] == n[(mid-1):][::-1]

if __name__ == '__main__':
    maxp = 0
    for f, s in itertools.product(range(1000, 0, -1), range(1000, 0, -1)):
        candidate = f*s
        if candidate > maxp and is_palindrome(candidate):
            maxp = candidate
    print("The answer to Euler Problem 4 is", maxp)