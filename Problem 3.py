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
    bound = math.sqrt(num)
    if num & 1 == 0:
        return False
    for cfactor in xrange(3, int(bound + 1)):
        if num % cfactor == 0:
            return False
    return True

if __name__ == '__main__':
    largest_factor = 0
    N = 600851475143777
    for candidate in range(3, int(math.ceil(math.sqrt(N)))):
        if N % candidate == 0:
            if isprime(candidate):
                largest_factor = candidate
            elif isprime(int(N / candidate)):
                largest_factor = int(N / candidate)
    print("The answer to Euler Probelm 3 is", largest_factor)