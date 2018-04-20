from __future__ import print_function
import sys
# Borrowed from scipy/lib/six.py (sort of)
if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range

res = sum(num for num in xrange(1, 1001) 
          if num % 3 == 0 or num % 5 == 0)
print("The answer to Euler Problem 1 is {}".format(res))

